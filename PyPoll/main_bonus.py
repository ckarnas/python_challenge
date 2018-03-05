#The program to run PyPoll
#Colleen Karnas-Haines
#3/2/2018

import os
import pandas as pd
import sys
csvpath = os.path.join("raw_data","election_data_1.csv")
csvpath2 = os.path.join("raw_data", "election_data_2.csv")

polling_data1 = pd.read_csv(csvpath)
polling_data2 = pd.read_csv(csvpath2)
frames = [polling_data1, polling_data2]
polling_data = pd.concat(frames)


#set up to write to file AND terminal
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("PollResults.txt", "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    

sys.stdout = Logger()



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

#bonus fun
#A list of counties
list_of_counties = polling_data["County"].unique()

each_county_total = {}
for county in list_of_counties:
    each_county_total[county]={}
    each_county_total[county]["Total"]=polling_data.loc[polling_data["County"]==county, "County"].count()
    each_county_total[county]["Win Total"]=(polling_data.loc[(polling_data["County"] == county) & (polling_data["Candidate"] == winner),"County"]).count()
    each_county_total[county]["Percent"] = round((each_county_total[county]["Win Total"]/each_county_total[county]["Total"]), 2)*100
                    
#Summary Stats
big_vote_county = max(each_county_total, key = lambda v: each_county_total[v]["Win Total"])
print(big_vote_county + " gave " + winner + " the most votes: " + str(each_county_total[big_vote_county]["Win Total"]) + ". But were they the happiest county?")
big_percent = max(each_county_total, key = lambda v: each_county_total[v]["Percent"])
if big_vote_county == big_percent:
    print("Yes!")
else:
    print("Interestingly, no.")
print("The happiest county is " + big_percent + " county, because they had highest percent of their citizens voting for Candidate " + winner)
print("A whopping " + str(each_county_total[big_percent]["Percent"]) + "% of " + big_percent + " citizens gave their votes to Candidate " + winner)

