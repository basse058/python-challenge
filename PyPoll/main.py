import os
import csv

csvpath = os.path.join( 'Resources', 'election_data.csv')

totalvotes = 0

print ("Election Results")
print ("-------------------------") 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
     #find total of profit/loss
          
    for row in csvreader:
        totalvotes += 1
        pltotal += int(row[1])
        #avgchange

    print("Total Votes: ", totalvotes)
    print("Total: ", "$",pltotal)