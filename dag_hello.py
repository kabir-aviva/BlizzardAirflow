from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'start_date': datetime(2025, 7, 23),
}

with DAG(
    dag_id='hello_world',
    default_args=default_args,
    schedule='@daily',  # Usa 'schedule' aquí, NO 'schedule_interval'
    catchup=False,
    tags=['example'],
) as dag:

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )
