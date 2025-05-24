import pandas as pd
import os
from get_csv_files import Get_Csv

class Consolidate(Get_Csv):
	"""docstring for Consolidate"""
	def __init__(self, directory):
		super(Consolidate, self).__init__(directory)
		self.file_names = self.get_csv()

	def consolidate(self):
		master_df = pd.DataFrame()

		try:
			for file in self.file_names:
				file_path = os.path.join(self.directory, file)
				df = pd.read_csv(file_path)

				if "Time" in df.columns:
					df["Time"] = pd.to_datetime(df["Time"])

					master_df = pd.concat([master_df, df], ignore_index=True)

				else:
					print(f"Skipping {file}: 'Time' column not found")

			master_df.drop_duplicates(subset="Time", inplace=True)  # Dropping duplicates
			master_df.to_csv(f"./master_merge/{self.directory}_master.csv", index=False)

		except Exception as e:
			print(f"Error reading {file_path}: {e}")

	def inner_join(self):
		master_df = None

		try:
			for file in self.file_names:
					file_path = os.path.join(self.directory, file)

					if '_' in file:
						unique_id = file.split('_')[0]
					else:
						unique_id = file.split('.')[0]

					df = pd.read_csv(file_path, parse_dates=["Time"])
					df["Date"] = df["Time"].dt.date
					df["Time"] = df["Time"].dt.time
					df.columns = [f"{unique_id}_{col}" if col != "Date" else "Date" for col in df.columns]

					if master_df is None:
						master_df = df
					else:
						if len(master_df) >= len(df):
							master_df = pd.merge(master_df, df, on="Date", how="left")
						else:
							master_df = pd.merge(master_df, df, on="Date", how="right")

			master_df = master_df.sort_values("Date").reset_index(drop=True)
			# master_df.dropna(inplace=True)
			master_df.to_csv("./master.csv", index=False)


		except Exception as e:
			# if "Length mismatch" in e:
			# 	print("Matching inter and intraday data")

			# else:
			# 	raise
			print(f"Error reading {file}: {e}")
			print("Note that the datetime column must be named Time and be formatted %Y-%m-%d %H:%M:%S")