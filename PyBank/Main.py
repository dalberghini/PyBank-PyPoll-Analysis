import os
import csv
date = []
profit_loss = []
p_ls = 0
change = 0
delta = []
date_average = []
Profit = 0
profit_date = ""
loss = 0
loss_date = ""
input_file = os.path.join("Resources", "budget_data.csv")
with open(input_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(int(row[1]))
        change = int(row[1]) - p_ls
        if change == int(row[1]):
            p_ls=int(row[1])
        elif change != int(row[1]):
            delta.append(change)
            p_ls = int(row[1])
            date_average.append(row[0])
data = zip(date_average, delta) 
for x in data:
    if int(x[1]) >=Profit:
        Profit = int(x[1])
        profit_date = str(x[0])
    if int(x[1]) <= loss:
        loss = int(x[1])
        loss_date = str(x[0])
average_change = sum(delta)/len(delta)
titles = [
    "Total Months: ",
    "Total: ",
    "Average Change: ",
    "Greatest Increase in Profits: ",
    "Greatest Decrease in Profits: "
]
results = [
     (len(date)),
     (sum(profit_loss)),
     (round(average_change,2)),
     (f'{profit_date} (${Profit})'),
     (f'{loss_date} (${loss})')
]
results_final = zip(titles, results)
print("Financial Analysis")
print("--------------------------------")
print(f'Total months: {len(date)}')
print(f'Total: ${sum(profit_loss)}')
print(f'Average Change: ${round(average_change,2)}')
print(f'Greatest Increase in Profits: {profit_date} (${Profit})')
print(f'Greatest Decrease in Profits: {loss_date} (${loss})')
output_file = os.path.join("Analysis", "results.csv")
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerows(results_final)
    