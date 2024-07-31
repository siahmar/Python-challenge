# Create script that analyzes the records to calculate: 
    # total number of months included in the dataset
import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csvreader(csvfile, delimiter = ',')
    print(csvreader)