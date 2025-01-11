import os
import logging
import sys


def setup_logger():
	logger = logging.getLogger(__name__)

	logger.setLevel(logging.DEBUG)

	logger_handler = logging.StreamHandler(sys.stdout)
	logger_handler.setLevel(logging.DEBUG)
	logger.addHandler(logger_handler)

	formatter = logging.Formatter(
		'%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s'
	)
	logger_handler.setFormatter(formatter)

	return logger

def get_connection_data(db_name):
	return {
	"HOST"	:	os.getenv(f"{db_name}_HOST"),
	"PORT"	:	os.getenv(f"{db_name}_PORT"),
	"USER"	:	os.getenv(f"{db_name}_USER"),
	"PASS"	:	os.getenv(f"{db_name}_PASS"),
	"DB"	:	os.getenv(f"{db_name}_DB"),
}

def execute_sql(adapter, file_name):
	# file = open(file_name)
	# sql_query = file.read()
	# file.close()
	with open(file_name) as sql_file:
		adapter.execute_commit_query(sql_file.read())


logger = setup_logger()

postgres_connection_data = get_connection_data("POSTGRES")
mysql_connection_data = get_connection_data("MYSQL")

DOCKER_DIR	= '/opt/airflow/dags/'
SQL_DIR		= 'sql/'

postgres_createAndPopulate_SQL	= f"{DOCKER_DIR}sql/postgres_createAndPopulate.sql"
mysql_create_tables_SQL			= f"{DOCKER_DIR}sql/mysql_create_tables.sql"

tables_to_replicate_YAML		= f"{DOCKER_DIR}tables_to_replicate.yaml"

vitrina_create_user_analytics_SQL			= f"{DOCKER_DIR}sql/vitrina_create_user_analytics.sql"
vitrina_create_product_performance_SQL		= f"{DOCKER_DIR}sql/vitrina_create_product_performance.sql"
vitrina_populate_user_analytics_SQL			= f"{DOCKER_DIR}sql/vitrina_populate_user_analytics.sql"
vitrina_populate_product_performance_SQL	= f"{DOCKER_DIR}sql/vitrina_populate_product_performance.sql"