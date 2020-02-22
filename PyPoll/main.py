import os 
import csv

#create the path and read it

csvpath = os.path.join("..", "resources", "election_data.csv")

output_path = os.path.join("..", "Analyses", "election_analysis.txt")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    header = next(csvreader)
    print(header)

    votes = []

    candidates = []

    for row in csvreader:

        votes.append(row[0])

    total_votes = len(votes)

with open(output_path,'w') as txtfile:
    




###analysis
print('Election Results')
print("-----------------")
print(f'Total Votes: {total_votes}')
print("-----------------")



