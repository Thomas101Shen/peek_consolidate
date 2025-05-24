import pandas as pd
import os

class Get_Csv(object):
	"""Parent class for other data operation classes"""
	def __init__(self, directory):
		super(Get_Csv, self).__init__()
		self.directory = directory

	def get_csv(self):
		csv_files = [f for f in os.listdir(self.directory) if f.endswith(".csv")]
		return csv_files