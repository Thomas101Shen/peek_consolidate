from peek_data import Peek_Data
from consolidate_data import Consolidate

peeker = None
consolidator = None
while True:
	operation = input("""Type A for peeking data
						\nB for consolidating tables containing same data from different times
						\nC for inner join different tables on same Time (assumed to be datetime)
						\nD to exit\n""")

	if operation != 'D':
		csv_dir = input("Input directory of csv data to operate on:\n")

	if operation == "A":
		if not peeker or csv_dir != peeker.directory: peeker = Peek_Data(csv_dir)
		peeker.peek()

	elif operation == "B":
		print("This will save the consolidated files in master_merge directory")
		if not consolidator or csv_dir != consolidator.directory:
			consolidator = Consolidate(csv_dir)
		consolidator.consolidate()

	elif operation == "C":
		print("This only works if all csv files are contained within the directory")
		print("This also removes all incomplete rows")
		if not consolidator or csv_dir != consolidator.directory:
			consolidator = Consolidate(csv_dir)
		consolidator.inner_join()

	elif operation == "D":
		break
	else:
		print("Invalid operation")


	print("\n")