from datetime import datetime

from airflow import DAG
# from airflow.providers.postgres.hooks.postgres import PostgresHook
# from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.operators.python import PythonOperator

from utils import vitrina_user_analytics_SQL, vitrina_product_perfomance_SQL, mysql_connection_data
from adapter_mysql import MySQL_adapter


def create_vitrina(vitrina_query_file):
	adapter = MySQL_adapter(mysql_connection_data)

	file = open(vitrina_query_file)
	sql_query = file.read()
	file.close()

	adapter.execute_commit_query(sql_query)


create_mysql_vitrina_dag = DAG(
	dag_id="3_Create_MySQL_Vitrina",
	start_date=datetime(2023, 12, 1),
	catchup=False,
	tags=["vitrina"],
)

create_vitrina_user_analytics_task = PythonOperator(
	task_id="create_vitrina_user_analytics_task",
	python_callable=create_vitrina,
	op_args=[vitrina_user_analytics_SQL],
	dag=create_mysql_vitrina_dag
)

create_vitrina_product_perfomance_task = PythonOperator(
	task_id="create_vitrina_product_perfomance_task",
	python_callable=create_vitrina,
	op_args=[vitrina_product_perfomance_SQL],
	dag=create_mysql_vitrina_dag
)

create_vitrina_user_analytics_task >> create_vitrina_product_perfomance_task
