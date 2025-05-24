# Overview
The code works best if the datetime column is called Time, peeking will work most of the time but the consolidation won't. If you do not have pandas, install it however you prefer. Then run `main.py` however you prefer.

The code will prompt you for 4 options. A will return metadata, and the head and tail of all csv files in a directory.
B will consolidate all data in a directory consisting similar data into one masterfile, append \_master.csv to it, and save it to master_merge.
C will consolidate all data in a directory consisting the same "Time" column into one masterfile, and name it 
D will terminate the program

This is meant to combine intraday and interday data

## Sample Usage
Run `python main.py`
When prompted, input `A`, and `example_prices`
You will see the sample intraday NQ data that I provided (some days are missing)
input `A` again, and `example_atr`
You will see more sample NQ data, this is daily ATR data

Try option `B` on each example directory, then `A` for `master_merge` to view the "master" csv tables
Then, run option `C` on `master_merge` and `master.csv` will appear in your current directory
Finally, run option `A` on `./`, and you will see the merged data.
The example ATR is missing data from March 16th, so you could run dropna on the master.csv file and you will see the daily ATR merged with intraday prices

## Warnings
Option C will keep rows that have NaN values. I thought this way gives more freedom. Feedback is welcomed. Also, is it risky for me to merge dataframes on left or right depending on which side has more instances? (I assume this way would enable intraday and interday data compatability but may introduce unforeseen errors down the line)