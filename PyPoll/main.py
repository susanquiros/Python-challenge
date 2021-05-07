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
    percentage = 0
    percentage_votes = []

        
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
        percentage = ((count_votes/Total_votes)*100)
        percentage_votes.append(percentage)
max_votes = max(votes)    
winner = unique_candidates[votes.index(max_votes)] 
#printing the results
print(f'Election Results')
print("-------------------------------")
print(f'Total Votes : {Total_votes}')
print("-------------------------------")
for y in range(len(unique_candidates)):
    print(f'{unique_candidates[y]}:Percentage: {round((percentage_votes[y]),2)}% Total votes:({votes[y]})')
print("----------------------------------------")
print(f'The winner is: {winner}')
print("----------------------------------------")

#writing my txt file
datafile = os.path.join (r'C:\Users\squiros\Python-challenge\PyPoll\Output\Res.electiondata.txt')
with open(datafile, "w") as outfile:
    outfile.write(f'Election Results\n')
    outfile.write("-------------------------------\n")
    outfile.write(f'Total Votes : {Total_votes}\n')
    outfile.write("-------------------------------\n")
    for y in range(len(unique_candidates)):
        outfile.write(f'{unique_candidates[y]}:Percentage: {round((percentage_votes[y]),2)}% Total votes:({votes[y]})\n')
    outfile.write("----------------------------------------\n")
    outfile.write(f'The winner is: {winner}\n')
    outfile.write("----------------------------------------\n")

 
          