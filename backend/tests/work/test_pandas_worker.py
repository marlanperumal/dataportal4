from typing import List
import pytest
import pandas as pd

from ...workers import CSVWorker, PandasWorker
from ...models.meta import Field, Table, TableHandle, TableWeight


@pytest.fixture
def table() -> Table:
    return Table(name="table")


@pytest.fixture
def table_handle(table: Table) -> TableHandle:
    return TableHandle(table=table, handle="table", index_handle="id")


@pytest.fixture
def fields(table: Table, table_handle: TableHandle) -> List[Field]:
    return [
        Field(table=table, name="ID", handle="id", table_handle=table_handle),
        Field(table=table, name="Weight", handle="weight", table_handle=table_handle),
        Field(table=table, name="A", handle="a", table_handle=table_handle),
        Field(table=table, name="B", handle="b", table_handle=table_handle),
        Field(table=table, name="C", handle="c", table_handle=table_handle),
    ]


@pytest.fixture
def table_weight(table: table, fields: List[Field]) -> TableWeight:
    return TableWeight(
        table=table, name="Individuals", index_field=fields[0], weight_field=fields[1]
    )


@pytest.fixture
def result_template() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "a": [1, 2],
            "b": [1, 1],
            "weight_sum": [1, 2],
            "value_sum": [1, 5],
            "zero_sum": [0, 0],
        }
    )


def test_connection():
    df = pd.read_csv("backend/tests/data/simple_data_0.csv")
    worker = PandasWorker(df)
    assert len(worker.df) == 3


def test_pandas_get_pivot_data(
    table_weight: TableWeight, fields: List[Field], result_template: pd.DataFrame
):
    df = pd.read_csv("backend/tests/data/simple_data_0.csv")
    worker = PandasWorker(df)

    df = worker.get_pivot_data(fields=fields[2:4], weight=table_weight, value=fields[4])

    assert df.equals(result_template)


def test_csv_get_pivot_data(
    table_weight: TableWeight, fields: List[Field], result_template: pd.DataFrame
):
    worker = CSVWorker("backend/tests/data/simple_data_0.csv")

    df = worker.get_pivot_data(fields=fields[2:4], weight=table_weight, value=fields[4])

    assert df.equals(result_template)
