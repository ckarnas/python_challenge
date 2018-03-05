#The program to run PyPoll
#Colleen Karnas-Haines
#3/2/2018

#
#
# I did some fun bonus work in the file named main_bonus.py
# Check it out!
#
#

import os
import sys
import pandas as pd
csvpath = os.path.join("raw_data","election_data_1.csv")
csvpath2 = os.path.join("raw_data", "election_data_2.csv")

polling_data1 = pd.read_csv(csvpath)
polling_data2 = pd.read_csv(csvpath2)
#polling_data.head()
#set up to write to file AND terminal
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("PollResults1.txt", "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    

sys.stdout = Logger()

frames = [polling_data1, polling_data2]

polling_data = pd.concat(frames)

#Calculating the total votes
total_votes = polling_data["Voter ID"].nunique()
#total_votes

#A list of candidates
list_of_candidates = polling_data["Candidate"].unique()
#list_of_candidates

#Make a list of candidate names and their percent of votes
each_candidate_percentage = {}
for candidate in list_of_candidates:
    each_candidate_percentage[candidate]=(polling_data.loc[polling_data["Candidate"] == candidate,"Candidate"].count() / total_votes) * 100

                                                        
#each_candidate_percentage

#Make a list of candidate names and their total votes
each_candidate_total = {}
for candidate in list_of_candidates:
    each_candidate_total[candidate]=polling_data.loc[polling_data["Candidate"] == candidate,"Candidate"].count() 

#each_candidate_total

#Find the candidate with the most votes 
winner = max(each_candidate_total, key=lambda key: each_candidate_total[key])
#winner

#combine our two lists (percentage and total)
from collections import defaultdict

combo = defaultdict(list)

for candidate in (each_candidate_total, each_candidate_percentage):
    for key, value in candidate.items():
        combo[key].append(value)

#combo

#Output
fancy_line = "----------------------"
print("Election Results")
print(fancy_line)
print("Total Votes: " + str(total_votes))
print(fancy_line)
for x in (list_of_candidates):
    print(x + ": " + str(round(combo[x][1],1)) + "% (" + str(combo[x][0]) + ")")
print(fancy_line)
print("Winner: " + winner)
print(fancy_line)

