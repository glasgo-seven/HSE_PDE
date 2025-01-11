from datetime import datetime
import yaml

from airflow import DAG
from airflow.operators.python import PythonOperator

from utils import tables_to_replicate_YAML, postgres_connection_data, mysql_connection_data
from adapter_postgres import Postgres_adapter
from adapter_mysql import MySQL_adapter


def postgres_select_table(table, columns):
	adapter = Postgres_adapter(postgres_connection_data)
	rows = adapter.execute_commit_query(
		f"SELECT {', '.join(f'"{column}"' for column in columns)} FROM {table}"
	)
	return rows

def mysql_insert_data(table, rows, columns):
	adapter = MySQL_adapter(mysql_connection_data)
	adapter.execute_commit_query(
		f"REPLACE INTO `{table}` ({', '.join(f'`{column}`' for column in columns)}) VALUES ({', '.join(['%s'] * len(rows[0]))})",
		rows
	)

def replicate_table(table, columns):
	mysql_insert_data(
		table,
		postgres_select_table(table, columns),
		columns
	)


transfer_data_postgres_to_mysql_dag = DAG(
	dag_id="2_Transfer_Data_Postgres_to_MySQL",
	start_date=datetime(2024, 12, 1),
	catchup=False,
	tags=["replication"],
)

file = open(tables_to_replicate_YAML, 'r')
tables_to_replicate = yaml.safe_load(file).get("tables_to_replicate")
file.close()

previous_task = None
for table in tables_to_replicate:
	current_task = PythonOperator(
		task_id=f"2x_Replicate_{table.get('table')}",
		python_callable=replicate_table,
		op_args=[table.get("table"), table.get("columns")],
		dag=transfer_data_postgres_to_mysql_dag
	)
	if previous_task:
		previous_task >> current_task
	previous_task = current_task
