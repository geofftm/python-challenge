import os
import csv

#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

csvpath = '/Users/geoffreymatis/Desktop/DS_Bootcamp/Git/python-challenge/PyBank/Resources/budget_data.csv'

with open(csvpath, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
