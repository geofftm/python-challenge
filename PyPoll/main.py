import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

candidates = []

with open(csvpath, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)

     for row in csvreader:
         candidates.append(row[1])
         print(len(candidates))
     


