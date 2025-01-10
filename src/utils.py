import os
import logging
import sys

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

logger_handler = logging.StreamHandler(sys.stdout)
logger_handler.setLevel(logging.DEBUG)
logger.addHandler(logger_handler)

formatter = logging.Formatter(
	'%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s'
)
logger_handler.setFormatter(formatter)

log_msg_err = lambda e: f"INTERNAL CODE ERROR - {e}"


# postgres_connection_data = 'POSTGRES'
postgres_connection_data = {
	"HOST"	:	os.getenv("POSTGRES_HOST"),
	"PORT"	:	os.getenv("POSTGRES_PORT"),
	"USER"	:	os.getenv("POSTGRES_USER"),
	"PASS"	:	os.getenv("POSTGRES_PASS"),
	"DB"	:	os.getenv("POSTGRES_DB"),
}

# mysql_connection_data = 'MYSQL'
mysql_connection_data = {
	"HOST"	:	os.getenv("MYSQL_HOST"),
	"PORT"	:	os.getenv("MYSQL_PORT"),
	"USER"	:	os.getenv("MYSQL_USER"),
	"PASS"	:	os.getenv("MYSQL_PASS"),
	"DB"	:	os.getenv("MYSQL_DB"),
}

DOCKER_DIR	= '/opt/airflow/dags/'
SQL_DIR		= 'sql/'

postgres_createAndPopulate_SQL	= f"{DOCKER_DIR}sql/postgres_createAndPopulate.sql"
mysql_create_tables_SQL			= f"{DOCKER_DIR}sql/mysql_create_tables.sql"
tables_to_replicate_YAML		= f"{DOCKER_DIR}tables_to_replicate.yaml"
vitrina_user_analytics_SQL		= f"{DOCKER_DIR}sql/vitrina_user_analytics.sql"
vitrina_product_perfomance_SQL	= f"{DOCKER_DIR}sql/vitrina_product_perfomance.sql"