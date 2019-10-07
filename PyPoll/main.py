#This is for PyPoll
#Import modules
import os
import csv

#Join dataset file (assumes file is in Resources subfolder)
election_data = os.path.join("Resources","election_data.csv")

#Create variables to process results
votes_total = 0
candidates []
candidates_votes
# define votes_can_total


#Access dataset
with open(election_data, newline="") as election_data_file:
    election_data_reader = csv.reader(election_data_file, delimiter=",")

    #Skip header row
    header = next(election_data_file)

    #Read through each remaining row
    for row in election_data_reader:

        #Update total vote count 
        votes_total +=1

        #Update candidate name list [2]

        #Update candidate vote total

# Calculate candidate vote perecent 

# Calculate winner

#Print the analysis to the terminal
print ("\nElection Results")
print ("-------------------------")
#print ("Total Votes: " + votes_total)
print ("-------------------------")
#print (candidates + ":" + votes_can_percent + "% (" + votes_can_total + ")") 
print ("----------------------- --")
#print ("Winner: " + winner)
print ("-------------------------")

#Export a text file with the results
f = open("PyPoll_analysis.text", "w+")
#repeat print list

  #Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------