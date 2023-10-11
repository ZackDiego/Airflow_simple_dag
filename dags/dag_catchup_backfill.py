import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator 


default_args = {
    "retries":5,
    "retry_delay":pendulum.duration(minutes=5),
    "owner":"Zack"
}

with DAG(
    'catchup_backfill_dag_v3',
    default_args=default_args,
    description='Simple print DAG',
    schedule_interval= "@daily",
    start_date=pendulum.datetime(2023, 8 ,6, 3),
    catchup = False
) as dag:
    bash_task = BashOperator(
        task_id="bash_task",
        bash_command='echo "Hi from bash operator"',
        # env: Optional[Dict[str, str]] = None,
        # output_encoding: str = 'utf-8',
        # skip_exit_code: int = 99,
    )
    bash_task