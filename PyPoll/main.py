import os 
import csv

#create the path and read it

csvpath = os.path.join("..", "resources", "election_data.csv")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    header = next(csvreader)
    print(header)

    votes = []

    for row in csvreader:

        votes.append(row[0])

    total_votes = len(votes)


###analysis
print('Election Results')
print("-----------------")
print(f'Total Votes: {total_votes}')
print("-----------------")



