import os
import csv
#Relative Path - error finding the csv file using this path so had to use full path
#csvpath = os.path.join(r'Python-challenge/PyPoll/Resources/election_data.csv')

#Full path
csvpath = os.path.join(r'/Users/siawashahmar/Desktop/Data Analytics Bootcamp/Python-challenge/PyPoll/Resources/election_data.csv')

with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

#Read data from csv and store as list
    raw_data = list(csv_reader)
    tot_votes = len(raw_data)

#Create empty lists to store entries from list comprehension   
    candidate_list = []
    tally = []

    for i in range (0, tot_votes):
        candidate_name = raw_data[i][2]
        tally.append(candidate_name)   
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
    tot_numb_candidates = len(candidate_list)
  

    vote = []
    percent = []
#Use list comprehension to determine votes for each candidate and calculate % of votes
    for k in range (0, tot_numb_candidates):
        candidate_name = candidate_list[k]
        vote.append(tally.count(candidate_name))
        vote_percent = vote[k]/tot_votes
        percent.append(vote_percent)

#find the candidate with most/max votes
winner = vote.index(max(vote))

#Print results
print("Election Results:")
print("___________________________________________")
print(f"Total Votes:    {tot_votes}")
print("___________________________________________")
print(f"{candidate_list[0]} : {percent[0]:%}  ({vote[0]})")
print(f"{candidate_list[1]} : {percent[1]:%}  ({vote[1]})")
print(f"{candidate_list[2]} : {percent[2]:%}  ({vote[2]})")
print("___________________________________________")
print(f"Winner: {candidate_list[winner]}")

#Prepare text file for export
results_textfile = (
    "Election Results:\n"
    "________________________________________\n"
    f"Total Votes:  {tot_votes}\n"
    "________________________________________\n"
    f"{candidate_list[0]} : {percent[0]:%}  ({vote[0]})\n"
    f"{candidate_list[1]} : {percent[1]:%}  ({vote[1]})\n"
    f"{candidate_list[2]} : {percent[2]:%}  ({vote[2]})\n"
    "___________________________________________\n"
    f"Winner: {candidate_list[winner]}\n"
)

with open ('Final_output.txt', 'w') as file:
    file.write(results_textfile)