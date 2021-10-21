from typing import List, Dict, Optional
from dataclasses import dataclass
import pandas as pd
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine import create_engine
from sqlalchemy import MetaData, Table as SqlTable
from sqlalchemy.sql.expression import case, select
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import Column
from ..models.meta import Field, TableWeight


class Worker:
    def get_pivot_data(
        self, fields: List[Field], weight: TableWeight, value: Optional[Field] = None
    ) -> pd.DataFrame:
        pass

    def pivot(
        self, rows: List[Field], cols: List[Field], weight: TableWeight, base: Field
    ) -> pd.DataFrame:
        pass

    def trend(
        self, fields: List[Field], weight: TableWeight, base: Field
    ) -> pd.DataFrame:
        pass


class SQLWorker(Worker):
    engine: Engine
    conn_uri: str

    def __init__(self, conn_uri: str):
        self.conn_uri = conn_uri
        self.engine = create_engine(self.conn_uri)

    def get_pivot_data(
        self, fields: List[Field], weight: TableWeight, value: Optional[Field] = None
    ) -> pd.DataFrame:
        metadata = MetaData()

        @dataclass
        class TableMeta:
            table: SqlTable
            index_column: Column

        field_columns = []
        tables: Dict[str, TableMeta] = {}

        def create_column(field: Field, tables: Dict[str, TableMeta]) -> Column:
            table_handle = field.table_handle
            if table_handle.handle in tables:
                table = tables[table_handle.handle].table
            else:
                table = SqlTable(table_handle.handle, metadata)
                index_column = Column(table_handle.index_handle)
                table.append_column(index_column)
                tables[table_handle.handle] = TableMeta(table, index_column)
            column = Column(field.handle)
            table.append_column(column)
            return column

        weight_column = create_column(weight.weight_field, tables)
        for field in fields:
            column = create_column(field, tables)
            field_columns.append(column)

        if value is not None:
            value_column = create_column(value, tables)
        else:
            value_column = 1

        query = select(
            *field_columns,
            func.sum(weight_column).label("weight_sum"),
            func.sum(weight_column * value_column).label("value_sum"),
            func.sum(weight_column * case((value_column.is_(None), 1), else_=0)).label(
                "zero_sum"
            ),
        )

        table_list = list(tables.values())
        for i, table in enumerate(table_list):
            if i == 0:
                query = query.select_from(table.table)
            else:
                query = query.join(
                    table.table, table_list[0].index_column == table.index_column
                )

        query = query.group_by(*field_columns).order_by(*field_columns)

        df = pd.read_sql(query, self.engine)
        return df


class PostgreSQLWorker(SQLWorker):
    def __init__(
        self,
        host: str,
        user: str,
        password: str,
        port: str = "5432",
        db: str = "postgres",
    ):
        conn_uri = f"postgresql://{user}:{password}@{host}:{port}/{db}"
        super().__init__(conn_uri)


class PandasWorker(Worker):
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_pivot_data(
        self, fields: List[Field], weight: TableWeight, value: Optional[Field] = None
    ) -> pd.DataFrame:
        weight_field = weight.weight_field.handle
        value_field = value.handle

        def agg(df: pd.DataFrame):
            d = {
                "weight_sum": df[weight_field].sum(),
                "value_sum": (df[weight_field] * df[value_field]).sum(),
                "zero_sum": df[df[value_field].isna()][weight_field].sum(),
            }
            return pd.Series(d, index=list(d))

        result = self.df.groupby(
            [field.handle for field in fields], as_index=False
        ).apply(agg)
        return result


class CSVWorker(PandasWorker):
    def __init__(self, filepath: str):
        self.df = pd.read_csv(filepath)
