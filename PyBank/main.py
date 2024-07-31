import os
import csv

#Relative Path
#csvpath = os.path.join(r'Python-challenge/PyBank/Resources/budget_data.csv)

#The relative path for the CSV file did not work so I had to copy the full path to get it to work on my sytem
csvpath = os.path.join(r'/Users/siawashahmar/Desktop/Data Analytics Bootcamp/Python-challenge/PyBank/Resources/budget_data.csv')

with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csv_reader)
    
#Declare empty lists 
    date = []
    profit_losses = []
    changes = []

#Use list comprehension to store date column in date list, and profit/losses in profit_losses list
    for row in csv_reader:
        date.append(row[0])
        profit_losses.append(float(row[1]))

# Counts the total legnth of date list
tot_months = len(date)

# Net total for profit/losses column
net_profit = sum(profit_losses)

# Using declared lists: Calculate the changes in profit/losses and store them in change list
for i in range(1, tot_months):
    difference = profit_losses[i] - profit_losses[i-1]
    changes.append(difference)

avg_change = sum(changes) / tot_months

# Find max increase and max decrease values and correspondign dates
max_increase = max(changes)
max_increase_date = date[changes.index(max_increase) + 1]
max_decrease = min(changes)
max_decrease_date = date[changes.index(max_decrease) + 1]

# Print the analysis results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {tot_months}")
print(f"Total Profit/Losses: ${net_profit:.0f}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase:.0f})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease:.0f})")

#Prepare text file for export

results_textfile = (
    "Financial Analysis\n"
    "-----------------------------\n"
    f"Total Months: {tot_months}\n"
    f"Total Profit/Losses: ${net_profit:.0f}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {max_increase_date} (${max_increase:.0f})\n"
    f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease:.0f})\n"
)

with open('Final_output.txt', 'w') as file: 
    file.write(results_textfile)