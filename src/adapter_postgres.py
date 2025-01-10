import os
import sys

import psycopg2

from adapter_abstract import Abstract_adapter
from utils import logger


class Postgres_adapter(Abstract_adapter):

	def get_cursor(self):
		connection = psycopg2.connect(
			dbname=self.DB,
			user=self.USER,
			password=self.PASS,
			host=self.HOST,
			port=self.PORT,
		)
		return super().get_cursor(connection)


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
			self.close()
