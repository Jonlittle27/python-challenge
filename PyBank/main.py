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

    greatest_increase = ["", 0]

    greatest_decrease = ["", 100000]


    csvheader = next(csvreader)

    previousRow = next(csvreader)

    previousRow = int(previousRow[1])
   

#creating the for loop - filling it the steps for total months and total price
    for row in csvreader:
        #Months
        newmonth = row[0]
        months.append(newmonth[0])
        
        #net total

        currentRow = int(row[1])
        net_total = net_total + currentRow   

        #price changes

        priceChange = currentRow - previousRow

        priceChanges.append(priceChange)

        previousRow = currentRow 

        #increase / decrease

        if priceChange > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = priceChange

        if priceChange < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = priceChange




    total_months = len(months) + 1

    average = round(sum(priceChanges) / len(priceChanges),2)





    # Printing the analysis

    print("Financial Analysis")
    print("------------------")
    print(f"Total Months = {total_months}")
    print(f"Total: ${net_total:,}")
    print(f"Average Price Change: ${average}")
    print(f"Greatest Increase in Profits:{greatest_increase}")
    print(f"Greatest Decrease in Profits:{greatest_decrease}")

output = os.path.join("..","Analyses","Financial_Analysis.txt")

with open(output, 'w') as text:
    text.write("Financial Analysis")
    text.write("\n")
    text.write(f"Total Months = {total_months}")
    text.write("\n")
    text.write(f"Total: ${net_total:,}")
    text.write("\n")
    text.write(f"Average Price Change: ${average}")
    text.write("\n")
    text.write(f"Greatest Increase in Profits:{greatest_increase}")
    text.write("\n")
    text.write(f"Greatest Decrease in Profits:{greatest_decrease}")


    


        

