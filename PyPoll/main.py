# Import modules
import os
import csv

# Set path for file
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Assigning values to variables before opening the csv file
row = 1
votes = 0
total_votes = 0
candidate = 0
candidate_names = [] #Create list
candidate_votes = {} #Create Dictionary
winning_vote = 0
winning_candidate = ''	

# Open the CSV
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	# Read the header row first (skip this step if there is now header)
	csv_header = next(csvreader)

	# Read through each row
	for row in csvreader:

		# Find total votes
		total_votes += 1

		candidate_name = row[2]

		# Create candidate list
		if candidate_name not in candidate_names:
			candidate_names.append(candidate_name)
			candidate_votes[candidate_name] = 0

		candidate_votes[candidate_name] += 1	

# Create and print output and file
with open('Polling_Analysis.txt', "w") as file:

	print("Election Results")
	print("-------------------------")
	print("Total Votes: ", total_votes)
	print("-------------------------")

	file.write(f"Election Results\n")
	file.write(f"-------------------------\n")
	file.write(f"Total Votes:{total_votes}\n")
	file.write(f"-------------------------\n")

	# Find vote percentage for each candidate
	for candidate in candidate_votes:
		votes = candidate_votes.get(candidate)
		vote_percent = (votes / total_votes) * 100

		# Find winner
		if (votes > winning_vote):
			winning_vote = votes
			winning_candidate = candidate			
		
		# Print each candidate, their % of the vote and total number of votes
		voter_output = f"{candidate}: {vote_percent:.3f}% ({votes})\n"     
		print(voter_output)
		file.write(f"{voter_output}\n")

	print("-------------------------")
	print("Winner: ", winning_candidate)
	print("-------------------------")
	file.write(f"-------------------------\n")
	file.write(f"Winner: {winning_candidate}\n")
	file.write(f"-------------------------\n")



