import os

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
