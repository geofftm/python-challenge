import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

months = 0
value = 0
totalProfitsLosses = 0
currentProfitLoss = 0
lastProfitLoss = 0


monthList = []
changeList = []
profitsLosses = []
valueList = []

with open(csvpath, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     
     for row in csvreader:
        months += 1
        currentProfitLoss = int(row[1])
        totalProfitsLosses += currentProfitLoss

        if months == 1:
            lastProfitLoss = currentProfitLoss
            continue
        else:
            change = currentProfitLoss - lastProfitLoss
            monthList.append(row[0])
            changeList.append(change)
            lastProfitLoss = currentProfitLoss
     
     changeSum = sum(changeList)
     averageChange = changeSum / (months - 1)
     maxChange = max(changeList)
     minChange = min(changeList)

     maxIdx = changeList.index(maxChange)
     minIdx = changeList.index(minChange)

     maxDate = monthList[maxIdx]
     minDate = monthList[minIdx]

     print("")
     print("Financial Analysis")
     print("----------------------------")
     print("")
     print(f"Total Months : {months}")
     print(f"Total: ${totalProfitsLosses}")
     print(f"Average Change: ${averageChange}")
     print(f"Greatest Increase in Profits: {maxDate} (${maxChange})")
     print(f"Greatest Decrease in Profits: {minDate} (${minChange})")

budget_data_analysis = os.path.join("budget_data_analysis.txt")
with open(budget_data_analysis, "w") as output:
     output.write("Financial Analysis\n")
     output.write("----------------------------\n")
     output.write("")
     output.write(f"Total Months : {months}\n")
     output.write(f"Total: ${totalProfitsLosses}\n")
     output.write(f"Average Change: ${averageChange}\n")
     output.write(f"Greatest Increase in Profits: {maxDate} (${maxChange})\n")
     output.write(f"Greatest Decrease in Profits: {minDate} (${minChange})\n")
    

     
  

    
     

