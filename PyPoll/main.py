import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)

     for row in csvreader:
         print(row[1])
     


