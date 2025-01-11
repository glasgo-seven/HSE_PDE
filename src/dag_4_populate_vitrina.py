from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from utils import vitrina_populate_user_analytics_SQL, vitrina_populate_product_performance_SQL, mysql_connection_data, execute_sql
from adapter_mysql import MySQL_adapter

# def populate_vitrina(vitrina_query_file):
# 	adapter = MySQL_adapter(mysql_connection_data)

# 	file = open(vitrina_query_file)
# 	sql_query = file.read()
# 	file.close()

# 	adapter.execute_commit_query(sql_query)


populate_mysql_vitrina_1_dag = DAG(
	dag_id="4.1_Populate_MySQL_Vitrina_user_analytics",
	start_date=datetime(2023, 12, 1),
	catchup=False,
	tags=["vitrina"],
)

populate_vitrina_user_analytics_task = PythonOperator(
	task_id="populate_vitrina_user_analytics_task",
	python_callable=execute_sql,
	op_args=[MySQL_adapter(mysql_connection_data), vitrina_populate_user_analytics_SQL],
	dag=populate_mysql_vitrina_1_dag
)

populate_vitrina_user_analytics_task


populate_mysql_vitrina_2_dag = DAG(
	dag_id="4.2_Populate_MySQL_Vitrina_product_performance",
	start_date=datetime(2023, 12, 1),
	catchup=False,
	tags=["vitrina"],
)

populate_vitrina_product_performance_task = PythonOperator(
	task_id="populate_vitrina_product_performance_task",
	python_callable=execute_sql,
	op_args=[MySQL_adapter(mysql_connection_data), vitrina_populate_product_performance_SQL],
	dag=populate_mysql_vitrina_2_dag
)

populate_vitrina_product_performance_task
