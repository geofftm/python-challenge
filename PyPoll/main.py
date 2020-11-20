import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

candidates = []

totalVotes = 0

with open(csvpath, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)

     for row in csvreader:
         candidates.append(row[2])
         totalVotes += 1
     print(totalVotes)
     print(sorted(candidates))

     
     
     


