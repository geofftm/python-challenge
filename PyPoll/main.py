#import dependencies

import os
import csv
from collections import Counter

#file path

csvpath = os.path.join('Resources', 'election_data.csv')

# setting empty lists to be used later to variables

candidates = []
voteCount = []

# set the total votes to 0 to count later in loop

totalVotes = 0

# open and read the csv file

with open(csvpath, 'r') as csvfile:
    # setting the delimiter on the comma as this is a csv file
     
     csvreader = csv.reader(csvfile, delimiter=',')
     
     # this will skip the header
     
     csv_header = next(csvreader)

     #loop through the file

     for row in csvreader:
         
         # append the candidates to the empty list 'candidates' each pass through the loop
         
         candidates.append(row[2])
         
         # count the total votes by adding a vote each pass through the loop
         
         totalVotes += 1

     # use the sort method to sort the list by candidate name

     sortedCandidates = sorted(candidates)

     # Use counter to give the total count of votes by each candidate

     countedCandidates = Counter (sortedCandidates)

     # use most_common() method to get the most - least counts and append the values to an empty list

     voteCount.append(countedCandidates.most_common())
     
     # loop through voteCount list and assign the vote totals to variables, from highest to lowest, using the index values of in the list of couples

     for i in voteCount:
         platinum = i[0][1]
         gold = i[1][1]
         silver = i[2][1]
         bronze = i[3][1]
     
     # loop through the voteCount list again assign the names to variables using the index value in the list of couples
         name1 = i[0][0]
         name2 = i[1][0]
         name3 = i[2][0]
         name4 = i[3][0]
     
     # calculating the percentages of the vote and formatting to 3  decimal places using the float value

     platinumPct = format((platinum)*100/(sum(countedCandidates.values())), '.3f')
     goldPct = format((gold)*100/(sum(countedCandidates.values())), '.3f')
     silverPct = format((silver)*100/(sum(countedCandidates.values())), '.3f')
     bronzePct = format((bronze)*100/(sum(countedCandidates.values())), '.3f')


     print("Election Results")
     print("-------------------------")
     print(f"Total Votes : {totalVotes}")
     print("-------------------------")
     # using f strings to build the strings showing name, perentage of the vote and total votes
     print(f"{name1}: {platinumPct}% ({platinum})")
     print(f"{name2}: {goldPct}% ({gold})")
     print(f"{name3}: {silverPct}% ({silver})")
     print(f"{name4}: {bronzePct}% ({bronze})")
     print("-------------------------")
     print(f"Winner: {name1}")
     print("-------------------------")

# write the results to a txt file
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

     
     
     


