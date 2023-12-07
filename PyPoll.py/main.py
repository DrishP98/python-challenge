#import

import os
import csv

#set file path
election_data_csv = "election_data.csv"

# Declaring the Variables/lists
 
total_votes = 0
candidates = []
candidate_votes = {}
winner_count = 0
winning_percentage = 0
winner = ""
candidate_results = []  

#open the csv file

with open(election_data_csv) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

#reading the first row
    header = next(csvreader)

# Print each row in the CSV file.
    for row in csvreader:
        
        # Add the total vote count
        total_votes += 1

        # Get the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidates:
            # Add the candidate name to the candidate list.
            candidates.append(candidate_name)

            # Finf candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

   #caluclate vote perecentage
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        result = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})")
        candidate_results.append(result)

    #Calculate winning vote count, percentage, and candidate.
        if (votes > winner_count) and (vote_percentage > winning_percentage):
            winner_count = votes
            winner = candidate
            winning_percentage = vote_percentage

#Print results 
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes:,}")
print(f"-------------------------")

#Print each candidate's result on a separate line
for result in candidate_results:
    print(result)

print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")
    
# Output files to text

file_to_output = "election_results_summary.txt"

with open(file_to_output, 'w') as file:
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {total_votes:,}\n")
    file.write("----------------------------\n")

# Write each candidate's result on a separate line
    for result in candidate_results:
        file.write(f"{result}\n")

    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
    file.close()




