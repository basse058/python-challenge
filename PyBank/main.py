import os
import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')

pltotal = 0
totalmo = 0
avgchange = 0
print ("Financial Analysis")
print ("-------------------------") 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
     #find total of profit/loss
          
    for row in csvreader:
        totalmo += 1
        pltotal += int(row[1])
        #avgchange

    print("Total Months: ", totalmo)
    print("Total: ", "$",pltotal)
    #print("Average Change: ", )
    #print("Greatest Increase in Profits: ", )
    #print("Greatest Decrease in Profits: ", )



#print (Totalsum)

#print (str(len(row[0])))



#def print_percentages(finance_data):
#    date = str(finance_data[0])
#     = int(finance_data[1])


#print(f"Total Months: {date}" )
#print(f"Total: {}")
#print(f"Average Change: {Average}")
#print(f"Greatest Increase in Profits: {}")
#print(f"Greatest Decrease in Profits: {}")


#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes


#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period