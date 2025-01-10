import os
# import sys

from utils import logger

class Abstract_adapter:
	def __init__(self, connection_data):
		logger.error(connection_data)
		self.HOST	= connection_data["HOST"]
		self.PORT	= connection_data["PORT"]
		self.USER	= connection_data["USER"]
		self.PASS	= connection_data["PASS"]
		self.DB		= connection_data["DB"]


	def get_cursor(self, connection):
		self.connection = connection
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
	
	def close(self):
		self.close_cursor()
		self.close_connection()


	def get_query(self, file):
		current_path = os.path.dirname(os.path.abspath(__file__))
		with open(current_path + file, 'r') as file:
			sql_query = file.read()
		return sql_query


	# def execute_custom_query(self, query):
	# 	try:
	# 		cursor = self.get_cursor()
	# 		cursor.execute(query)
	# 		rows = cursor.fetchall()
	# 		logger.debug(f"Get new records: {len(rows)}")
	# 		return rows
	# 	except Exception as e:
	# 		logger.error(f"Error: {e}")
	# 		sys.exit(1)
	# 	finally:
	# 		self.close()