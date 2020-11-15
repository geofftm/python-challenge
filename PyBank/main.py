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
        month = row[0]
        profits_losses = row[1]
        totalProfitsLosses += int(profits_losses)
        change = int(profits_losses) - value
        #print(change)
        value = int(row[1])
        monthList.append(months)
        profitsLosses.append(profits_losses)
        valueList.append(value)
        changeList.append(int(change))
    
    
     print("Total Months: " + str(len(monthList)))
     print("Total: $" + str(totalProfitsLosses))
     
     negativeSum = sum(i for i in changeList if i < 0)

     positiveSum = sum(j for j in changeList if j > 0)

     print(positiveSum)
     print(negativeSum)
    

     
  

    
     

