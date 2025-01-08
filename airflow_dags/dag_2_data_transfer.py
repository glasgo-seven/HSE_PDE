from datetime import datetime
import yaml

from airflow import DAG
from airflow.operators.python import PythonOperator

# from usecase.pg_select import pg_fetch_table
# from usecase.mysql_insert_data import mysql_insert_data


from postgres_adapter import Postgres_adapter
def pg_fetch_table(table_name, columns):
    columns_string = ', '.join(f'"{col}"' for col in columns)
    sql_query = f"SELECT {columns_string} FROM {table_name}"
    connection = Postgres_adapter()
    rows = connection.execute_custom_query(sql_query)
    return rows


from mysql_adapter import MySQL_adapter
def mysql_insert_data(table_to_insert, rows, columns):
    columns_string = ', '.join(f'`{col}`' for col in columns)
    placeholders = ', '.join(['%s'] * len(rows[0]))  # One placeholder for each column
    sql_query = f"REPLACE INTO `{table_to_insert}` ({columns_string}) VALUES ({placeholders})"
    connection = MySQL_adapter()
    connection.execute_commit_query(sql_query, rows)


def load_replicate_config(config_file="/opt/airflow/dags/tables_to_replicate.yaml"):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config


def replicate_table(table, columns):
    fetch_result = pg_fetch_table(table, columns)
    mysql_insert_data(
        table_to_insert=table,
        rows=fetch_result,
        columns=columns
    )


with DAG(
    dag_id="2_Transfer_Data_Postgres_to_MySQL",
    start_date=datetime(2024, 12, 1),
    catchup=False,
    tags=["replication"],
) as dag:
    tables_to_replicate = load_replicate_config().get("tables_to_replicate")
    previous_task = None
    for table in tables_to_replicate:
        current_task = PythonOperator(
            task_id=f"2x_Replicate_{table.get('table')}",
            python_callable=replicate_table,
            op_args=[table.get("table"), table.get("columns")], 
        )
        if previous_task:
            previous_task >> current_task
        previous_task = current_task
