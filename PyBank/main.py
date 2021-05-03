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
    total_amount = []
    sum_total_amount = 0

    for row in csvreader:
        print (row)
        count_months = count_months + 1
        total_amount.append(int(row[1]))
        sum_total_amount= sum(total_amount) 
    #knowing what type of data it's my column 1    
        #print(type (row [1]))
 
print ("Financial Analysis")
print ("------------------")   
print(f"Total Months: {count_months}")
print(f'total:{sum_total_amount}')
print("average change")
print("Greatest Increase in Profits")
print("Greatest Decrease in Profits")
#print(total_amount)
    