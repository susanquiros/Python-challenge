#Importing the file
import os
import csv
#specifying the path 
csvpath = os.path.join(r"C:\Users\squiros\Python-challenge\PyPoll\Resources\PyPoll.electiondata.csv")


#opening the file 
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        #getting ride of the header
    csv_header = next(csvreader, None)
    #print(csv_header)

    #setting up my variables
    count_votes = 0
    Total_votes = 0
    candidates= []
    unique_candidates = []
    votes = []

        
    for row in csvreader:
        #print(row)
        #total number of votes
        Total_votes =  Total_votes + 1
        #getting the candidates
        candidates.append(row[2])
    for x in set(candidates):
        unique_candidates.append(x)
      #counting the total votes by candidate
        count_votes = candidates.count(x)
        votes.append(count_votes)
print(votes)

    
print(Total_votes) 
print(unique_candidates)          