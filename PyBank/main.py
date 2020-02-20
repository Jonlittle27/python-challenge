import os 
import csv

#create the path and read it

csvpath = os.path.join("..", "resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#setting an open array to hold the months data and filling it
    months = []
    
    net_total = 0

    priceChanges = []


    csvheader = next(csvreader)

#creating the for loop - filling it the steps for total months and total price
    for row in csvreader:

        newmonth = row[0].split("-")
        months.append(newmonth[0])

        currentRow = int(row[1])
        net_total = net_total + currentRow      


    total_months = len(months)

    # Printing the analysis

    print("Financial Analysis")
    print("------------------")
    print(f"Total Months = {total_months}")
    print(f"Total: ${net_total}")
    print("Average Price Change:")
    


        

