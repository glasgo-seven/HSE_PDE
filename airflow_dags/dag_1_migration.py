from datetime import datetime

from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.operators.python import PythonOperator

# from utils.pg_initial_migration import pg_init_migration
# from utils.mysql_initial_migration import mysql_init_migration


from postgres_adapter import Postgres_adapter
def postgres_createAndPopulate():
    connection = Postgres_adapter()
    with open("/opt/airflow/dags/sql/postgres_createAndPopulate.sql") as file:
        sql_query = file.read()
    rows = connection.execute_commit_query(sql_query)

from mysql_adapter import MySQL_adapter
def mysql_create_tables():
    connection = MySQL_adapter()
    with open("/opt/airflow/dags/sql/mysql_create_tables.sql") as file:
        sql_query = file.read()
    rows = connection.execute_commit_query(sql_query)


with DAG(
    dag_id="1_Initial_Migration",
    start_date=datetime(2023, 12, 1),
    catchup=False,
    tags=["migration"],
) as dag:
        
        postgres_createAndPopulate_task = PythonOperator(
            task_id="postgres_migrate",
            python_callable=postgres_createAndPopulate,
        )

        mysql_create_tables_task = PythonOperator(
            task_id="mysql_migrate",
            python_callable=mysql_create_tables,
        )

postgres_createAndPopulate_task >> mysql_create_tables_task
