from ...workers import PostgreSQLWorker


def test_connection():
    worker = PostgreSQLWorker(
        host="localhost",
        user="postgres",
        password="postgres",
        port="5432",
        db="postgres",
    )

    worker.engine.connect()
    worker.engine.execute("SELECT 1")
    worker.engine.dispose()
