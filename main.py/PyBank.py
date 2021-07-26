# Module for reading CSV files
import csv
# First we'll import the os module
import os
import numpy as np

# FIGURE OUT THE FILEPATH ON YOUR COMPUTER
csvpath = "Instructions/PyPoll/Resources/election_data.csv"

# read in the CSV data into memory - a list of lists
with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
     # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # store all my rows as a list of lists
    all_rows = []
    for row in csvreader:
        # clean rows and cast the second colum to an integer
        temp_row = row
        temp_row[1] = int(temp_row[1])
        
        all_rows.append(temp_row)

# print(all_rows)

# grab length of data set
total_votes = len(all_rows)

# sum of the second column
all_profits = [x[1] for x in all_rows]
sum_profit = sum(all_profits)

changes = []
for i in range(len(all_rows) - 1):
    curr_profit = all_rows[i][1]
    next_profit = all_rows[i +1][1]

    change = next_profit - curr_profit
    changes.append(change)

# get average changes
average_change = (sum(changes)/len(changes))
average_change2 = np.mean(changes)

max_change = max(changes)
min_change = min(changes)

# get change indexes
max_change_indx = changes.index(max_change) + 1
max_change_numpy = np.argmax(changes) + 1
max_month = all_rows[max_change_indx][0]

min_change_indx = changes.index(min_change) + 1
min_change_array = np.argmin(changes) + 1
min_month = all_rows[min_change_indx][0]

out_path = "pybank.txt"
with open(out_path, "w") as f:
    f.write(f"FINACIAL ANALYSIS\n")
    f.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    f.write(f"TOTAL VOTES   :                                       {total_votes}\n")
    f.write(f"A COMPLETE LIST OF CANDIDATES WHO RECEIVED VOTESS:    ${sum_profit}\n")
    f.write(f"THE TOTAL NUMBER OF VOTES EACH CANDIDATE WON:         ${round(average_change, 2)}\n")
    f.write(f"THE WINNER OF THE ELECTION BASED ON POPULAR VOTE:     {max_month} ($ {max_change})\n")