# Import modules
import os
import csv

# Set path for file
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Assigning values to variables before opening the csv file
total_months = 1
profit_sum = 0
row = 1
previous_change = 0
net_change_list = []

max_change = 0
max_date = ''
min_change = 0
min_date = ''

# Open the CSV
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	# Read the header row first
	csv_header = next(csvreader)
	
	# Assigning values with the csv file open, before reading each row
	first_row = next(csvreader)
	previous_change = int(first_row[1])
	profit_sum = previous_change

	# Read through each row
	for row in csvreader:		

		# Find total number of months
		total_months += 1 

		# Find total profit
		profit_change = int(row[1])
		profit_sum += profit_change

		# Append list with net change (to find average change)
		net_change = profit_change - previous_change
		previous_change = profit_change
		net_change_list.append(net_change)

		# Find max and min values
		if(profit_change > max_change):
			max_change = profit_change
			max_date = row[0]
		
		if(profit_change < min_change):
			min_change = profit_change
			min_date = row[0]

# Find average change
average_change = sum(net_change_list) / len(net_change_list)

# Create and print output and file
with open('Financial_Analysis.txt', "w") as f:
	output = (
	f'Financial Analysis\n'
	f'----------------------------\n'
	f'Total Months: {total_months}\n'
	f'Total: ${profit_sum}\n'
	f'Average Change: ${average_change:.2f}\n'
	f'Greatest Increase in Profits: ({max_date}) ${max_change}\n'
	f'Greatest Decrease in Profits: ({min_date}) ${min_change}\n'
	)

	print(output)
	f.write(output)



