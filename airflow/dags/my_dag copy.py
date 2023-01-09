from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def helloWorld():
    print("Hello world!")

with DAG(dag_id="hello_world_dag_2",
         start_date=datetime(2021,1,1),
         schedule_interval="@hourly",
         catchup=False) as dag:
    task1 = PythonOperator(
        task_id="hello_world",
        python_callable=helloWorld)