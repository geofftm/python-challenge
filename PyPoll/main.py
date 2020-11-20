import os
import csv
from collections import Counter

csvpath = os.path.join('Resources', 'election_data.csv')

candidates = []

totalVotes = 0

with open(csvpath, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)

     for row in csvreader:
         candidates.append(row[2])
         totalVotes += 1
     
     counted = Counter(candidates)
     print("Election Results")
     print("-------------------------")
     print(f"Total Votes : {totalVotes}")
     print(f"Khan: {counted['Khan']}")
     print(counted)
     

     
     
     


