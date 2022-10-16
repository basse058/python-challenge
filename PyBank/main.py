import os
import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')

pltotal = 0
totalmo = 0
avchange = 0
increase = 0
decrease = 0
profit = 0
AvgDiff = 0
print ("Financial Analysis")
print ("-------------------------") 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
 
     #find totals for months and profits/losses        
    for row in csvreader:
        totalmo += 1
        pltotal += int(row[1])
    
    #find average change month-to-month, greatest increase, and greatest decrease
    for i in range(1,(profit)):
        avchange == (profit[i] - profit[i-1])
        AvgDiff = sum(avchange)/len(avchange)
        increase = max(avchange)
        decrease = min(avchange)
    
     #print    
    print("Total Months: ", totalmo)
    print("Total: $", pltotal)
    print("Average Change: ", AvgDiff)
    print("Greatest Increase in Profits: ", increase)
    print("Greatest Decrease in Profits: ", decrease)



#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes


#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period