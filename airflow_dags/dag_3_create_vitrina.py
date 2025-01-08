from datetime import datetime

from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.operators.python import PythonOperator

# from usecase.data_marts import sale_analisys

from mysql_adapter import MySQL_adapter
def create_vitrina():
    connection = MySQL_adapter()
    with open("/opt/airflow/dags/sql/vitrina.sql") as file:
        sql_query = file.read()
    rows = connection.execute_commit_query(sql_query)


with DAG(
    dag_id="3_Create_MySQL_Vitrina",
    start_date=datetime(2023, 12, 1),
    catchup=False,
    tags=["vitrina"],
) as dag:
        create_vitrina_task = PythonOperator(
            task_id="create_vitrina",
            python_callable=create_vitrina,
        )

create_vitrina_task
