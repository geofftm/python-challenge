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

     for i in voteCount:
         platinum = i[0][1]
         gold = i[1][1]
         silver = i[2][1]
         bronze = i[3][1]

         name1 = i[0][0]
         name2 = i[1][0]
         name3 = i[2][0]
         name4 = i[3][0]
     
     platinumPct = format((platinum)*100/(sum(countedCandidates.values())), '.3f')
     goldPct = format((gold)*100/(sum(countedCandidates.values())), '.3f')
     silverPct = format((silver)*100/(sum(countedCandidates.values())), '.3f')
     bronzePct = format((bronze)*100/(sum(countedCandidates.values())), '.3f')

     
     #less dynamic way. go into counter object and grab values from keys and run the math that way.
     #trying a more dynamic way.
     
    #  kahnTotal = countedCandidates['Khan']
    #  correyTotal = countedCandidates['Correy']
    #  liTotal = countedCandidates['Li']
    #  oTotal = countedCandidates["O'Tooley"]
    
    #  kahnAvg = (kahnTotal / totalVotes) * 100
    #  correyAvg = (correyTotal / totalVotes) * 100
    #  liAvg = (liTotal / totalVotes) * 100
    #  oAvg = (oTotal / totalVotes) * 100

     
     

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
     
 
         

     #print(sortedCandidates)
     print(name1)
     print(name2)
     print(name3)
     print(name4)
     print(platinumPct)
     print(goldPct)
     print(silverPct)
     print(bronzePct)
     print("Election Results")
     print("-------------------------")
     print(f"Total Votes : {totalVotes}")
     print("-------------------------")
     print(f"{name1}: {platinumPct}% ({platinum})")
     print(f"{name2}: {goldPct}% ({gold})")
     print(f"{name3}: {silverPct}% ({silver})")
     print(f"{name4}: {bronzePct}% ({bronze})")
     print("-------------------------")
     print(f"Winner: {name1}")
     print("-------------------------")
    
election_analysis = os.path.join("Analysis", "election_analysis.txt")
with open(election_analysis, "w") as output:
    output.write("Election Results\n")
    output.write("----------------------------\n")
    output.write("")
    output.write(f"Total Votes : {totalVotes}\n")
    output.write("-------------------------\n")
    output.write(f"{name1}: {platinumPct}% ({platinum})\n")
    output.write(f"{name2}: {goldPct}% ({gold})\n")
    output.write(f"{name3}: {silverPct}% ({silver})\n")
    output.write(f"{name4}: {bronzePct}% ({bronze})\n")
    output.write("-------------------------\n")
    output.write(f"Winner: {name1}\n")
    output.write("-------------------------\n")

     
     
     


