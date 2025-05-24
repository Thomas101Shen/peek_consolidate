import pandas as pd
import os
from get_csv_files import Get_Csv

class Peek_Data(Get_Csv):
	"""Return head and metadata about csv files"""
	def __init__(self, directory):
		super(Peek_Data, self).__init__(directory)
		self.csv_files = self.get_csv()

	def peek(self):

		for file in self.csv_files:
			file_path = os.path.join(self.directory, file)
			print(f"\n{'='*40}\nFILE: {file}\n{'='*40}")

			try:
				try:
					df = pd.read_csv(file_path, parse_dates=["Time"])  # If data is not in %Y-%m-%d %H:%M:%S format will need to use to_datetime instead
				except ValueError as e:
					if "Missing column" in str(e):
						df = pd.read_csv(file_path)
					else:
						raise

				print('\n[HEAD]')
				print(df.head())

				print("\n[TAIL]")
				print(df.tail())

				print('\n[INFO]')
				df.info()

				print('\n[DESCRIBE]')
				try:
					print(df.describe(include='all', datetime_is_numeric=True))
				except TypeError:
					# If datetime_is_numeric parameter isn't available
					print(df.describe(include='all'))

			except Exception as e:
				print(f"Error reading {file_path}: {e}")