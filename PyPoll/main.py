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

        
    for row in csvreader:
        #print(row)
        #total number of votes
        Total_votes =  Total_votes + 1
        #getting the candidates
        candidate.append(row[2])

print(Total_votes)        