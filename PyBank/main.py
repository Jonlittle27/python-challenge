import os 
import csv

#create the path and read it

csvpath = os.path.join("..", "resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#setting an open array to hold the months data and filling it
    months = []
    
    net_total = 0
    csvheader = next(csvreader)

#creating the for loop and filling it the steps
    for row in csvreader:
        
        newmonth = row[0].split("-")
        months.append(newmonth[0])

        net_total = net_total + int(row[1])
        


    total_months = len(months)

    # Printing the analysis

    print("Financial Analysis")
    print("------------------")
    print(f"Total Months = {total_months}")
    print(f"Total: ${net_total}")


        

