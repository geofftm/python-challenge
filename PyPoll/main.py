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
     kahnTotal = counted['Khan']
     correyTotal = counted['Correy']
     liTotal = counted['Li']
     oTotal = counted["O'Tooley"]
    
     kahnAvg = (kahnTotal / totalVotes) * 100
     correyAvg = (correyTotal / totalVotes) * 100
     liAvg = (liTotal / totalVotes) * 100
     oAvg = (oTotal / totalVotes) * 100

     countedList = counted.most_common()

    #  candidates_votes_list = []
    #  for key, value in counted():
    #    # print(key, value)
    #     for i in range(value):
    #         candidates_votes_list.append(key)

     for ele in counted:
        #print(ele,counted[ele])
        countedList.append(counted[ele])

     print("Election Results")
     print("-------------------------")
     print(f"Total Votes : {totalVotes}")
     print(f"Khan: {counted['Khan']}")
     print(counted)
     print(round(oTotal, 2))
     print(round(kahnAvg, 2))
     print(round(correyAvg, 2))
     print(round(liAvg, 2))
     print(round(oAvg, 2))
     print(countedList)

     
     
     


