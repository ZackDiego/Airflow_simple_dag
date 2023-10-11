from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'Zack',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
    'catchup':False
}

def getName(ti):
    ti.xcom_push(key = "firstName", value = "John")
    ti.xcom_push(key = "lastName", value = "Wick")

def greet(ti):
    firstName = ti.xcom_pull(task_ids = "get_name", key = "firstName")
    lastName = ti.xcom_pull(task_ids = "get_name", key = "lastName")
    print(f"Hello {firstName} {lastName}, how are you")

with DAG(
    default_args=default_args,
    dag_id='python_operator_w_xcom',
    description='Our first dag using python operator',
    start_date=datetime(2023, 8, 6, 14, 0),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=getName
    )


    task2 >> task1