from __future__ import annotations
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

GCS_BUCKET_NAME = 'blizzard-airflow-artifacts'

with DAG(
    dag_id="dag_de_prueba",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    schedule=None,
    tags=["poc", "gcs"],
) as dag:
    # Tarea 1: Imprime un saludo
    tarea_de_saludo = BashOperator(
        task_id="tarea_de_saludo",
        bash_command='echo "Hola Airflow! La PoC funciona."',
    )

    # Tarea 2: Lista el contenido del bucket de GCS
    listar_archivos_gcs = BashOperator(
        task_id="listar_archivos_gcs",
        bash_command=f"gsutil ls gs://{GCS_BUCKET_NAME}/dags",
    )

    tarea_de_saludo >> listar_archivos_gcs