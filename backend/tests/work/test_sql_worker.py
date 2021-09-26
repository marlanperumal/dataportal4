import pandas as pd

from ...workers import SQLWorker
from ...models.meta import Field, Table, TableHandle, TableWeight


def test_connection():
    worker = SQLWorker("sqlite:///:memory:")
    worker.engine.connect()
    result = worker.engine.execute("SELECT 1").scalar()
    assert result == 1


def test_get_pivot_data(client):
    worker = SQLWorker("sqlite:///:memory:")

    filename_1 = "backend/tests/data/simple_data_1.csv"
    df = pd.read_csv(filename_1)
    df.to_sql("table1", worker.engine)

    filename_2 = "backend/tests/data/simple_data_2.csv"
    df = pd.read_csv(filename_2)
    df.to_sql("table2", worker.engine)

    table = Table(name="table")
    table_handle_1 = TableHandle(table=table, handle="table1", index_handle="id")
    table_handle_2 = TableHandle(table=table, handle="table2", index_handle="id")

    fields = [
        Field(table=table, name="ID", handle="id", table_handle=table_handle_1),
        Field(table=table, name="Weight", handle="weight", table_handle=table_handle_1),
        Field(table=table, name="A", handle="a", table_handle=table_handle_1),
        Field(table=table, name="B", handle="b", table_handle=table_handle_2),
        Field(table=table, name="C", handle="c", table_handle=table_handle_1),
    ]

    table_weight = TableWeight(
        table=table, name="Individuals", index_field=fields[0], weight_field=fields[1]
    )

    df = worker.get_pivot_data(fields=fields[2:4], weight=table_weight, value=fields[4])

    assert df.equals(
        pd.DataFrame(
            {
                "a": [1, 2],
                "b": [1, 1],
                "weight_sum": [1, 2],
                "value_sum": [1, 5],
                "zero_sum": [0, 0],
            }
        )
    )

    worker.engine.dispose()
