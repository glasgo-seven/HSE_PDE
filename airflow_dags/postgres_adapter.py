import os
import logging
import sys
import psycopg2


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_handler = logging.StreamHandler(sys.stdout)
logger_handler.setLevel(logging.DEBUG)
logger.addHandler(logger_handler)
formatter = logging.Formatter(
    '%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s')
logger_handler.setFormatter(formatter)


postgres_conn_id = {
    "host": os.getenv("PG_HOST"),
    "port": os.getenv("PG_PORT"),
    "user": os.getenv("PG_USER"),
    "password": os.getenv("PG_PASSWORD"),
    "dbname": os.getenv("PG_DB"),
}

class Postgres_adapter:

    def __init__(self, connection=postgres_conn_id):
        self.PG_DB = connection.get("dbname", "default_db") 
        self.PG_USER = connection.get("user", "default_user")  
        self.PG_PWD = connection.get("password", "default_password")  
        self.PG_HOST = connection.get("host", "localhost")  
        self.PG_PORT = connection.get("port", 5432)  


    def get_cursor(self):
        self.connection = psycopg2.connect(
            dbname=self.PG_DB,
            user=self.PG_USER,
            password=self.PG_PWD,
            host=self.PG_HOST,
            port=self.PG_PORT,
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


    def execute_commit_query(self, query):
        try:
            cursor = self.get_cursor()
            cursor.execute(query)
            self.connection.commit()
            logger.debug("Query executed successfully.")
            if cursor.description:
                rows = cursor.fetchall()
                logger.debug(f"Get new records: {len(rows)}")
                return rows
            return None
        except Exception as e:
            logger.error(f"Error: {e}")
            sys.exit(1)
        finally:
            self.close_cursor()
            self.close_connection()
