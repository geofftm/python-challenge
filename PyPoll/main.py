import os
import csv
from collections import Counter

csvpath = os.path.join('Resources', 'election_data.csv')

candidates = []
voteCount = []

totalVotes = 0

with open(csvpath, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)

     for row in csvreader:
         candidates.append(row[2])
         totalVotes += 1
     
     sortedCandidates = sorted(candidates)
     
     countedCandidates = Counter (sortedCandidates)
     
     voteCount.append(countedCandidates.most_common())
     
     #less dynamic way. go into counter object and grab values from keys and run the math that way.
     #trying a more dynamic way.
     
     kahnTotal = countedCandidates['Khan']
     correyTotal = countedCandidates['Correy']
     liTotal = countedCandidates['Li']
     oTotal = countedCandidates["O'Tooley"]
    
     kahnAvg = (kahnTotal / totalVotes) * 100
     correyAvg = (correyTotal / totalVotes) * 100
     liAvg = (liTotal / totalVotes) * 100
     oAvg = (oTotal / totalVotes) * 100

     
     

    #  candidates_votes_list = []
    #  for key, value in counted():
    #    # print(key, value)
    #     for i in range(value):
    #         candidates_votes_list.append(key)

    #  for ele in counted:
    #     print(ele)
        #countedList.append(counted[ele])

    #  for i, j in countedListSort:
    #      voteCount.append(i)
    #      voteCount.append(j)
     
 
         

     print(sortedCandidates)
     print(voteCount)
     print("Election Results")
     print("-------------------------")
     print(f"Total Votes : {totalVotes}")
     print(f"Khan: {countedCandidates['Khan']}")
     print(round(oTotal, 2))
     print(round(kahnAvg, 2))
     print(round(correyAvg, 2))
     print(round(liAvg, 2))
     print(round(oAvg, 2))


    #  print(countedList)
    #  print(countedListSort)

     
     
     


