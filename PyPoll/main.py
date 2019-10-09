#This is for PyPoll
#Import modules
import os
import csv

#Join dataset file (assumes file is in Resources subfolder)
election_data = os.path.join("Resources","election_data.csv")

#Create variables and lists to tack results
votes_total = 0

#Create candidate related lists
candidates_list = []
candidates_votes = []
votes_percent = []
votes_round = []

#Access dataset to identify candidates and do overall vote count
with open(election_data, newline="") as election_data_file:
    election_data_reader = csv.reader(election_data_file, delimiter=",")

    #Skip header row
    header = next(election_data_file)

    #Read through each remaining row
    for row in election_data_reader:

        #Update total vote count 
        votes_total +=1

        #If new candidate append lists [2]
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            candidates_votes.append(0)
            votes_percent.append(0)
            votes_round.append(0)

#Access dataset second time to get votes per candidate
with open(election_data, newline="") as election_data_file:
    election_data_reader = csv.reader(election_data_file, delimiter=",")

    #Skip header row
    header = next(election_data_file)
    
    #get vote counts per candidate
    for row_two in election_data_reader:
        for i in range(len(candidates_list)):
            if candidates_list[i] ==row_two[2]:
                candidates_votes[i] +=1

#Calculate winner
#Populate winner variables with first candidate for comparing votes
winner = candidates_list[0]
win_votes = candidates_votes[0]

#Compare votes one at a time
for j in range(len(candidates_list)):
    if candidates_votes[j] > win_votes:
        #Update winner variables
        winner = candidates_list[j]
        win_votes = candidates_votes[j]

# Calculate candidate vote perecent and get 3 decimal points (round doesn't work here)
for k in range (len(candidates_votes)):
    votes_percent[k] = (candidates_votes[k]/votes_total)*100
    votes_percent[k] = '%.3f' % votes_percent[k] 

#Print the analysis to the terminal
print ("\nElection Results")
print ("-------------------------")
print ("Total Votes: " + str(votes_total))
print ("-------------------------")
for l in range(len(candidates_list)):
    print(candidates_list[l] + ":  " + str(votes_percent[l]) + "% (" + str(candidates_votes[l]) + ")") 
print ("-------------------------")
print ("Winner: " + winner)
print ("-------------------------")

#Export a text file with the results
f = open("PyPoll_analysis.text", "w+")
f.write ("\nElection Results")
f.write ("\n-------------------------")
f.write ("\nTotal Votes: " + str(votes_total))
f.write ("\n-------------------------")
for l in range(len(candidates_list)):
    f.write("\n" + candidates_list[l] + ":  " + str(votes_percent[l]) + "% (" + str(candidates_votes[l]) + ")") 
f.write ("\n-------------------------")
f.write ("\nWinner: " + winner)
f.write ("\n-------------------------")
