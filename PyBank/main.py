#Import modules
import os
import csv

#Join file (assumes file is in Resources subfolder)
budget_data = os.path.join("Resources","budget_data.csv")

#Create variables to track results
months = 0
net_income = 0
avg_change = 0
greast_increse = 0
greatest_decrease = 0

#Read dataset
with open(budget_data, newline="") as budget_data_file:
    budget_data_reader = csv.reader(budget_data_file, delimiter=",")

    #Skip first row
    header = next(budget_data_file)

    #Read through each row
    for row in budget_data_reader:

#The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

#  * The total number of months included in the dataset

#  * The net total amount of "Profit/Losses" over the entire period

#  * The average of the changes in "Profit/Losses" over the entire period

#  * The greatest increase in profits (date and amount) over the entire period

#  * The greatest decrease in losses (date and amount) over the entire period


  



# print the analysis to the terminal 

print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: ")
print ("Total: ")
print ("Average Change: ")
print ("Greatest Increase in Profits: ")
print ("Greatest Decrease in Profits: ")

  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)

# export a text file with the results.



