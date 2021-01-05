import os
import csv
voter_id = []
candidate = []
counter_can0= 0
counter_can1 = 0
counter_can2 = 0
counter_can3 = 0
votes = []
percent = []
input_file = os.path.join("Resources","election_data.csv")
with open(input_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    for row in csvreader:
        voter_id.append(row[0])
        if row[2] not in candidate:
            candidate.append(row[2])
        if row[2] == candidate[0]:
            counter_can0 = 1 + counter_can0
        elif row[2] == candidate[1]:
            counter_can1 = 1 + counter_can1
        elif row[2] == candidate[2]:
            counter_can2 = 1 + counter_can2
        elif row[2] == candidate[3]:
            counter_can3= 1 + counter_can3
total = len(voter_id)
votes.append(counter_can0)
votes.append(counter_can1)
votes.append(counter_can2)
votes.append(counter_can3)
results = zip(candidate, votes)
for x in votes:
    percentage = (x/total)
    percentage  = "{:.3%}".format(percentage)
    percent.append(percentage)
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
    print(f'Winner:')
    print("-------------------------")
Election_results()