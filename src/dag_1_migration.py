from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from utils import postgres_createAndPopulate_SQL, mysql_create_tables_SQL, postgres_connection_data, mysql_connection_data, execute_sql
from adapter_postgres import Postgres_adapter
from adapter_mysql import MySQL_adapter


# def postgres_createAndPopulate():
# 	connection = Postgres_adapter(postgres_connection_data)

# 	file = open(postgres_createAndPopulate_SQL, 'r')
# 	sql_query = file.read()
# 	file.close()

# 	connection.execute_commit_query(sql_query)

# def mysql_create_tables():
# 	connection = MySQL_adapter(mysql_connection_data)
	
# 	file = open(mysql_create_tables_SQL, 'r')
# 	sql_query = file.read()
# 	file.close()

# 	connection.execute_commit_query(sql_query)


initial_migration_dag = DAG(
	dag_id="1_Initial_Migration",
	start_date=datetime(2023, 12, 1),
	catchup=False,
	tags=["migration"],
)

postgres_createAndPopulate_task = PythonOperator(
	task_id="postgres_migrate",
	python_callable=execute_sql,
	op_args=[Postgres_adapter(postgres_connection_data), postgres_createAndPopulate_SQL],
	dag=initial_migration_dag
)

mysql_create_tables_task = PythonOperator(
	task_id="mysql_migrate",
	python_callable=execute_sql,
	op_args=[MySQL_adapter(mysql_connection_data), mysql_create_tables_SQL],
	dag=initial_migration_dag
)


postgres_createAndPopulate_task >> mysql_create_tables_task
