#import libs and dependencies.
import csv
import os
from pathlib import Path

#specifcy paths.
input_file = Path("Resources/election_data.csv")
output_file = Path("Analysis/election_analysis.txt")

#set variables.
total_votes = 0
candidates = []
cand_votes = {}
winner = ""
winning_votes = 0

#read CSV.
with open(input_file) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #read headers
    csv_header = next(reader)
    #print(f"CSV Header: {csv_header}")
    
#find total votes.
    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            cand_votes[candidate_name] = 0
        cand_votes[candidate_name] += 1
    #print first 4 lines of ouptut in terminal.
    print(f"Election Results\n")
    print(f"--------------------------------\n")
    print(f"Total Votes: {total_votes}\n")
    print(f"--------------------------------\n")    
#candidates, their pecetnage of the votes, and their share of the votes to txt file.
with open(output_file, "w") as txt_file:    
    txt_file.write(f"Election Results\n")
    txt_file.write(f"----------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write(f"----------------------\n")
    #find percent, vote counts, for candidates' summaries.
    for candidate_name in cand_votes:
        votes = cand_votes.get(candidate_name)
        vote_perc = (votes) / (total_votes) * 100
        cand_results = (f"{candidate_name}: {vote_perc:.3f}% ({votes:})\n")
        #print to terminal and txt file.
        print(cand_results)
        txt_file.write(cand_results)
        #print(cand_results)
        #declaring the winner using vote count.
        if (votes > winning_votes):
            winning_votes = votes
            winner = candidate_name
    txt_file.write(f"----------------------\n")
    txt_file.write(f"Winner: {winner}\n")
print(f"--------------------------------\n")        
print("Winner: " + winner)