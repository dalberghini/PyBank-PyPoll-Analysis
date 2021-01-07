# Using a csv file and Windows OS, so modules imported
import os
import csv
#Creation of lists and variables for first iteration of code
voter_id = []
candidate = []
#Line 26 uncommented to determine number of candidates, then matching number of vote counters created
counter_can0= 0
counter_can1 = 0
counter_can2 = 0
counter_can3 = 0
votes = []
percent = []
#Lists created for clean csv viewing
total_csv = ["Total Votes: "]
winner_csv = ["Winner: "]
#importing csv file from local repo and storing header
input_file = os.path.join("Resources","election_data.csv")
with open(input_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
#Searching through csv file to determine number of total voters and number of candidates
    for row in csvreader:
        voter_id.append(row[0])
        if row[2] not in candidate:
            candidate.append(row[2])
#print(candidate)
#Four candidates found and vote counters added for each candidate, update vote counters based on number of candidates if used for a different election
        if row[2] == candidate[0]:
            counter_can0 = 1 + counter_can0
        elif row[2] == candidate[1]:
            counter_can1 = 1 + counter_can1
        elif row[2] == candidate[2]:
            counter_can2 = 1 + counter_can2
        elif row[2] == candidate[3]:
            counter_can3= 1 + counter_can3
#Total votes found and Votes list created based on csv file
total = len(voter_id)
total_csv.append(total)
votes.append(counter_can0)
votes.append(counter_can1)
votes.append(counter_can2)
votes.append(counter_can3)
#Vote percentage formatted, list created, and comparison of results to determine winner
for x in votes:
    percentage = (x/total)
    percentage  = "{:.3%}".format(percentage)
    percent.append(percentage)
if percent[0] > percent[1] and percent[0] > percent[2] and percent[0] > percent[3]:
    winner = candidate[0]
if percent[1] > percent[0] and percent[1] > percent[2] and percent[1] > percent[3]:
    winner = candidate[1]
if percent[2] > percent[0] and percent[2] > percent[1] and percent[2] > percent[3]:
    winner = candidate[2]
if percent[3] > percent[0] and percent[3] > percent[1] and percent[3] > percent[2]:
    winner = candidate[3]
winner_csv.append(winner)
#Candidates, percent of votes, and votes for each candidate zipped together
results_csv = zip(candidate, percent, votes)
#Election_results function defined, not entirely neccessary, but code looks cleaner with defintion indentation
def Election_results():
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {total}')
    print("-------------------------")
    print(f'{candidate[0]} {percent[0]} ({counter_can0})')
    print(f'{candidate[1]}: {percent[1]} ({counter_can1})')
    print(f'{candidate[2]}: {percent[2]} ({counter_can2})')
    print(f"{candidate[3]}: {percent[3]} ({counter_can3})")
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")
#Results of election printed to terminal
Election_results()
#Output csv file created
output_file = os.path.join("Analysis", "results.csv")
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(total_csv)
    writer.writerows(results_csv)
    writer.writerow(winner_csv)
