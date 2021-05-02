#importing CSV file
import os
import csv
#specifying the path
csvpath= os.path.join(r"C:\Users\squiros\Python-challenge\PyBank\Resources\PyBank.data.csv")

#opening the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    for row in csvreader:
        print (row)
    #knowing what type of data it's my column 1    
    print(type (row [1]))
