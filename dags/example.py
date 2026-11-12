"""An example DAG. Replace it with your own."""

from datetime import datetime

from airflow.sdk import dag, task


@dag(schedule=None, start_date=datetime(2026, 1, 1), catchup=False, tags=["example"])
def example():
    @task
    def hello() -> str:
        return "Hello from Airflow on Wodby"

    hello()


example()
