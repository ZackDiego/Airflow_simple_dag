import pendulum
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator 


default_args = {
    "retries":5,
    "retry_delay":pendulum.duration(minutes=5),
    "owner":"Zack"
}

with DAG(
    'dag_w_postgres_v3',
    default_args=default_args,
    description='Simple print DAG',
    schedule_interval= "0 0 * * *",
    start_date=pendulum.datetime(2023, 8 ,5, 3),
    catchup = True
) as dag:
    task1 = PostgresOperator(
        task_id = "create_table_in_postgres",
        postgres_conn_id = "postgres_localhost",
        sql = """
            CREATE TABLE if not exists dag_runs(
                dt date,
                dag_id character varying,
                primary key  (dt, dag_id)
            )
        """
    )
    task2 = PostgresOperator(
        task_id = "insert_data_to_postgres",
        postgres_conn_id = "postgres_localhost",
        sql = """
            INSERT INTO dag_runs (dt, dag_id) values ('{{ ds }}', '{{ dag.dag_id}}')
        """
    )

    task3 = PostgresOperator(
        task_id = "delete_postgres_data",
        postgres_conn_id = "postgres_localhost",
        sql = """
            DELETE FROM dag_runs WHERE dt = '{{ ds }}' AND dag_id = '{{ dag.dag_id }}';
        """
    )

    task1 >> task3 >> task2