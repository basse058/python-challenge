# Import libraries and dependencies
import csv
import os
from pathlib import Path

# Specify the paths of input and output files
input_file = Path("Resources/budget_data.csv")
output_file = Path("Analysis/budget_analysis.txt")

# Initialize the variables
total_months = 0
month_of_change = []
list_of_net_change = []
greatest_increase = ["",0]
greatest_decrease = ["",10000000000000000000]
total_net = 0

# Read the csv file
with open(input_file) as budget_data:
    reader = csv.reader(budget_data)

    # Read the headers
    header = next(reader)

    # Extract information for first row
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1])

    # Loop through all the rows in csv file
    for row in reader:

        # Update the total
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # Update the net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        list_of_net_change = list_of_net_change + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the greates increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greates decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the average net change
average_net_change = round(sum(list_of_net_change) / len(list_of_net_change),2)

print(f"Financial Analysis\n")
print(f"--------------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: ${total_net}\n")
print(f"Average Change: ${average_net_change}\n")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
# Write the results file to a text file
with open(output_file, "w") as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"--------------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${average_net_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")