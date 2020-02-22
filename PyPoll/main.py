import os 
import csv

#create the import path and read it

csvpath = os.path.join("..", "resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    header = next(csvreader)
#setting the empty lists to hold the for loop values
    votes = []

    khan = []
    correy = []
    li = []
    tooley = []
#For loop to get total votes
    for row in csvreader:

        votes.append(row[0])

        #If statement to create a list of all the occurrences of the 
        #candidate names
        if row[2] == "Khan":
            khan.append(row[2])
        elif row[2] == "Correy":
            correy.append(row[2])
        elif row[2] == "Li":
            li.append(row[2])
        elif row[2] == "O'Tooley":
            tooley.append(row[2])
   
#Converting list lengths into a variable for vote totals and percentages 
total_votes = len(votes)

khan_total = len(khan)
khan_percent = round((khan_total/total_votes)*100,0)

correy_total = len(correy)
correy_percent = round((correy_total/total_votes)*100,0)

li_total = len(li)
li_percent = round((li_total/total_votes)*100,0)

tooley_total = len(tooley)
tooley_percent = round((tooley_total/total_votes)*100,0)



##analysis
print('Election Results')
print("-----------------")
print(f'Total Votes: {total_votes}')
print("-----------------")
print(f"Khan: {khan_percent} ({khan_total})")
print(f"Correy: {correy_percent} ({correy_total})")
print(f"Li: {li_percent} ({li_total})")
print(f"O'Tooley: {tooley_percent}% ({tooley_total})")
print("-----------------")
print("Winner: Khan")
print("-----------------")

##Text File setting the path and writing into the new text

output_path = os.path.join("..", "Analyses", "Election_Analysis.txt")

with open(output_path,'w') as text:
    text.write('Election Results')
    text.write('\n')
    text.write("-----------------")
    text.write('\n')
    text.write(f'Total Votes: {total_votes}')
    text.write('\n')
    text.write("-----------------")
    text.write('\n')
    text.write(f"Khan: {khan_percent} ({khan_total})")
    text.write('\n')
    text.write(f"Correy: {correy_percent} ({correy_total})")
    text.write('\n')
    text.write(f"Li: {li_percent} ({li_total})")
    text.write('\n')
    text.write(f"O'Tooley: {tooley_percent}% ({tooley_total})")
    text.write('\n')
    text.write("-----------------")
    text.write('\n')
    text.write("Winner: Khan")
    text.write('\n')
    text.write("-----------------")





