import os
import csv

#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

csvpath = '/Users/geoffreymatis/Desktop/DS_Bootcamp/Git/python-challenge/PyBank/Resources/budget_data.csv'

with open(csvpath, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     monthList = []
     profitsLosses = []
     totalProfitsLosses = 0
     for columns in csvreader:
        months = columns[0]
        profits_losses = columns[1]
        totalProfitsLosses += int(columns[1])
        monthList.append(months)
        profitsLosses.append(profits_losses)
     print("Total Months: " + str(len(monthList)))
     print("Total: $" + str(totalProfitsLosses))
    
