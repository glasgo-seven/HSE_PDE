import mysql.connector
import os
import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_handler = logging.StreamHandler(sys.stdout)
logger_handler.setLevel(logging.DEBUG)
logger.addHandler(logger_handler)
formatter = logging.Formatter(
    '%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s')
logger_handler.setFormatter(formatter)


mysql_conn_id = {
    "host": os.getenv("MYSQL_HOST"),
    "port": os.getenv("MYSQL_PORT"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "dbname": os.getenv("MYSQL_DB"),
}


class MySQL_adapter:

    def __init__(self, connection=mysql_conn_id):
        self.MYSQL_DB = connection.get("dbname", "default_db")
        self.MYSQL_USER = connection.get("user", "default_user")
        self.MYSQL_PWD = connection.get("password", "default_password")
        self.MYSQL_HOST = connection.get("host", "localhost")
        self.MYSQL_PORT = connection.get("port", 3306)

    def get_cursor(self):
        self.connection = mysql.connector.connect(
            database=self.MYSQL_DB,
            user=self.MYSQL_USER,
            password=self.MYSQL_PWD,
            host=self.MYSQL_HOST,
            port=self.MYSQL_PORT,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def close_cursor(self):
        if hasattr(self, 'cursor'):
            self.cursor.close()
        return True

    def close_connection(self):
        if hasattr(self, 'connection'):
            self.connection.close()
        return True

    def get_query(self, file):
        current_path = os.path.dirname(os.path.abspath(__file__))
        with open(current_path + file, 'r') as file:
            sql_query = file.read()
        return sql_query


    def execute_custom_query(self, query):
        try:
            cursor = self.get_cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            logger.debug(f"Get new records: {len(rows)}")
            return rows
        except Exception as e:
            logger.error(f"Error: {e}")
            sys.exit(1)
        finally:
            self.close_cursor()
            self.close_connection()


    def execute_commit_query(self, query, params=None):
        try:
            cursor = self.get_cursor()
            if params:
                cursor.executemany(query, params)
            else:
                for result in cursor.execute(query, multi=True):
                    logger.debug(f"Running query: {result.statement}")
                    if result.with_rows:
                        rows = result.fetchall()
                        logger.debug(f"Rows fetched: {rows}")
            self.connection.commit()
            logger.debug("All queries executed and committed successfully.")
        except Exception as e:
            logger.error(f"Error: {e}")
            sys.exit(1)
        finally:
            self.close_cursor()
            self.close_connection()