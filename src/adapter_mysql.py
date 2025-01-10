import sys

import mysql.connector

from adapter_abstract import Abstract_adapter
from utils import logger


class MySQL_adapter(Abstract_adapter):

	def get_cursor(self):
		connection = mysql.connector.connect(
			database=self.DB,
			user=self.USER,
			password=self.PASS,
			host=self.HOST,
			port=self.PORT,
		)
		return super().get_cursor(connection)


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
			self.close()