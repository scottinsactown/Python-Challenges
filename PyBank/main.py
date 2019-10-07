#Import modules
import os
import csv

#Join file (assumes file is in Resources subfolder)
budget_data = os.path.join("Resources","budget_data.csv")

#Create variables to track results
months = 0
net_income = 0
avg_change = 0
last_month = 0
monthly_change = 0
greatest_increase = 0
greatest_decrease = 0

#Access dataset
with open(budget_data, newline="") as budget_data_file:
    budget_data_reader = csv.reader(budget_data_file, delimiter=",")

    #Skip first row
    header = next(budget_data_file)

    #Read through each row
    for row in budget_data_reader:

        #Update months
        months += 1 

        #Update net_income 
        net_income += int(row[1])

        #Update monthly_change
        monthly_change = int(row[1]) - last_month
        last_month = int(row[1])
        #Tracking for avg_change
        total_change += monthly_change

        #Check greatest values
        if monthly_change > greatest_increase:
            greatest_increase = monthly_change
            greatest_increase_date = row[0]

        if monthly_change < greatest_decrease:
            greatest_decrease = monthly_change
            greatest_decrease_date = row[0]


avg_change = total_change/months
  
# print the analysis to the terminal 
print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: " + str(months))
print ("Total: $" + str(net_income))
print ("Average Change: $"+str(avg_change))
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



