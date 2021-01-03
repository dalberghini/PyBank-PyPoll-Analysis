import os
import csv
voter_id = []
candidate = []
counter_Khan = 0
counter_Correy = 0
counter_Li = 0
counter_OTooley = 0
counter_other = 0
votes = []
percent = []
input_file = os.path.join("Resources","election_data.csv")
with open(input_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    for row in csvreader:
        voter_id.append(row[0])
        candidate.append(row[2])
        if row[2] == "Khan":
            counter_Khan = 1 + counter_Khan
        elif row[2] == "Correy":
            counter_Correy = 1 + counter_Correy
        elif row[2] == "Li":
            counter_Li = 1 + counter_Li
        elif row[2] == "O'Tooley":
            counter_OTooley = 1 + counter_OTooley 
        else:
            counter_other = 1 + counter_other
total = len(voter_id)
votes.append(counter_Correy)
votes.append(counter_Khan)
votes.append(counter_Li)
votes.append(counter_OTooley)
votes.append(counter_other)
for x in votes:
    percentage = (round(((x/total)*100),1))
    percent.append(percentage)
def Election_results():
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {total}')
    print("-------------------------")
    print(f'Khan: ({counter_Khan})')
    print(f'Correy: ({counter_Correy})')
    print(f'Li: ({counter_Li})')
    print(f"O'Tooley: ({counter_OTooley})")
    print("-------------------------")
    
    print("-------------------------")
Election_results()