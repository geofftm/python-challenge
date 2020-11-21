#import dependencies

import os
import csv

# file path

csvpath = os.path.join('Resources', 'budget_data.csv')

# setting the variables to 0 to count values in the for loop

months = 0
value = 0
totalProfitsLosses = 0
currentProfitLoss = 0
lastProfitLoss = 0


# creating variables of empty lists

monthList = []
changeList = []
profitsLosses = []
valueList = []

# opening the csv file and reading it

with open(csvpath, 'r') as csvfile:
    # setting the delimiter on the comma as this is a csv file
     csvreader = csv.reader(csvfile, delimiter=',')
     #this will skip the header
     csv_header = next(csvreader)
     # loop through the file
     for row in csvreader:
        # counting months
        months += 1
        # grabbing the current value in the Profit/Losses Colum
        currentProfitLoss = int(row[1])
        #totaling the profit/losses
        totalProfitsLosses += currentProfitLoss
        # conditional statement that will make sure not to try to calucate the change since there was no prior value to calculate against
        if months == 1:
            lastProfitLoss = currentProfitLoss
            continue
        else:
            # this statement calculates the change by subtracting the prior value of the profits/losses column from the current value in profits/losses column
            change = currentProfitLoss - lastProfitLoss
            #append the current month to the list of months each pass through the loop
            monthList.append(row[0])
            #append the change calculation to the list of changes each pass through the loop
            changeList.append(change)
            lastProfitLoss = currentProfitLoss
     #calculating the sum of the changes, the average change, the highest change and the minium change
     changeSum = sum(changeList)
     # formatting so the average change will be shown with 2 decimal points in a float
     averageChange = format(changeSum / (months - 1), '.2f')
     maxChange = max(changeList)
     minChange = min(changeList)
     #index values of the largest and smallest changes
     maxIdx = changeList.index(maxChange)
     minIdx = changeList.index(minChange)
     # getting the date of the largest and smallest changes using the index
     maxDate = monthList[maxIdx]
     minDate = monthList[minIdx]
    # print the the text
     print("")
     print("Financial Analysis")
     print("----------------------------")
     print("")
     # using f strings to build the strings to show total months, total profits losses, average change, and dates of highest and lowest changes
     print(f"Total Months : {months}")
     print(f"Total: ${totalProfitsLosses}")
     print(f"Average Change: ${averageChange}")
     print(f"Greatest Increase in Profits: {maxDate} (${maxChange})")
     print(f"Greatest Decrease in Profits: {minDate} (${minChange})")
    #export the text
budget_data_analysis = os.path.join("Analysis", "budget_data_analysis.txt")
with open(budget_data_analysis, "w") as output:
     output.write("Financial Analysis\n")
     output.write("----------------------------\n")
     output.write("")
     output.write(f"Total Months : {months}\n")
     output.write(f"Total: ${totalProfitsLosses}\n")
     output.write(f"Average Change: ${averageChange}\n")
     output.write(f"Greatest Increase in Profits: {maxDate} (${maxChange})\n")
     output.write(f"Greatest Decrease in Profits: {minDate} (${minChange})\n")
    

     
  

    
     

