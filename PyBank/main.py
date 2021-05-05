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
    previous_month = 0
    current_month = 0
    Profit = []
    Months_avg = []

    for row in csvreader:
        #print (row)
        count_months = count_months + 1
        total_amount.append(int(row[1]))
        sum_total_amount= sum(total_amount) 
        #starting with the avg
        current_month = int(row[1])
        if count_months == 1:
          previous_month = current_month
          continue
        else:
          temp_profit = current_month - previous_month
         # Creating the list of the months
          Months_avg.append(row[0])
         #creating the list of the profit
          Profit.append(temp_profit)
         #calculating for the last month
          previous_month = current_month
       

#summarizing the profit
summarize = sum(Profit)
avg= round(summarize/(count_months -1),2)

#getting the Max
Max_profit = max(Profit)
increase_position = Profit.index(Max_profit)
increase_fecha = Months_avg[increase_position]
#getting the Min
Min_profit = min (Profit)
decrease_position = Profit.index(Min_profit)
decrease_fecha= Months_avg[decrease_position]
        
        


    #knowing what type of data it's my column 1    
        #print(type (row [1]))
 
print ("Financial Analysis")
print ("------------------")   
print(f"Total Months: {count_months}")
print(f'total:{sum_total_amount:,}')
print(f"average change:{avg:,}")
print(f"Greatest Increase in Profits: {increase_fecha} amount: {Max_profit:,}")
print(f"Greatest Decrease in Profits: {decrease_fecha} amount: {Min_profit:,}")
#print(increase_fecha)
#print(decrease_fecha)
#print(Max_profit)
#print(Min_profit)
#print(total_amount)
#print(summarize)
   