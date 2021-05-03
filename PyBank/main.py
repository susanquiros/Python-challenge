#importing CSV file
import os
import csv
#specifying the path
csvpath= os.path.join(r"C:\Users\squiros\Python-challenge\PyBank\Resources\PyBank.data.csv")

#opening the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

     #getting ride of of the header
    csv_header = next(csvreader, None)


      #variables
    count_months = 0 

    for row in csvreader:
        print (row)
        count_months = count_months + 1
    #knowing what type of data it's my column 1    
    print(type (row [1]))

#

  








    
print ("Financial Analysis")
print ("------------------")   
print(f"Total Months: {count_months}")
print("average change")
print("Greates Increase in Profits")
print("Greates Decrease in Profits")
    