from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from utils import vitrina_create_user_analytics_SQL, vitrina_create_product_performance_SQL, mysql_connection_data, execute_sql
from adapter_mysql import MySQL_adapter


# def create_vitrina(vitrina_query_file):
# 	adapter = MySQL_adapter(mysql_connection_data)

# 	file = open(vitrina_query_file)
# 	sql_query = file.read()
# 	file.close()

# 	adapter.execute_commit_query(sql_query)


create_mysql_vitrina_1_dag = DAG(
	dag_id="3.1_Create_MySQL_Vitrina_user_analytics",
	start_date=datetime(2023, 12, 1),
	catchup=False,
	tags=["vitrina"],
)

create_vitrina_user_analytics_task = PythonOperator(
	task_id="create_vitrina_user_analytics_task",
	python_callable=execute_sql,
	op_args=[MySQL_adapter(mysql_connection_data), vitrina_create_user_analytics_SQL],
	dag=create_mysql_vitrina_1_dag
)

create_vitrina_user_analytics_task


create_mysql_vitrina_2_dag = DAG(
	dag_id="3.2_Create_MySQL_Vitrina_product_performance",
	start_date=datetime(2023, 12, 1),
	catchup=False,
	tags=["vitrina"],
)

create_vitrina_product_performance_task = PythonOperator(
	task_id="create_vitrina_product_performance_task",
	python_callable=execute_sql,
	op_args=[MySQL_adapter(mysql_connection_data), vitrina_create_product_performance_SQL],
	dag=create_mysql_vitrina_2_dag
)

create_vitrina_product_performance_task
