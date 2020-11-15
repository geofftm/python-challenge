import os
import csv

#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

csvpath = '/Users/geoffreymatis/Desktop/DS_Bootcamp/Git/python-challenge/PyBank/Resources/budget_data.csv'

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
     
    #  profitsLosses = []
    # valueList = []
    #  changeList = []
    #  totalProfitsLosses = 0
     for row in csvreader:
        months += 1
        currentProfitLoss = int(row[1])
        #month = row[0]
        #profits_losses = row[1]
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


        # change = int(profits_losses) - value
        # #print(change)
        # value = int(row[1])
        # monthList.append(months)
        # profitsLosses.append(profits_losses)
        # valueList.append(value)
        # changeList.append(int(change))
     print(changeList)
     print(f"Total Months : {months}")
     print(f"Total: ${totalProfitsLosses}")
     print(f"Average Change: ${averageChange}")
     print(maxChange)
     print(minChange)
    
    #  print("Total Months: " + str(len(monthList)))
    #  print("Total: $" + str(totalProfitsLosses))
     
    #  negativeSum = sum(i for i in changeList if i < 0)

    #  positiveSum = sum(j for j in changeList if j > 0)

    #  print(positiveSum)
    #  print(negativeSum)
    

     
  

    
     

