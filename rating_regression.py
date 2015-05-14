import csv


f = open('feature_averages_final.csv')
csv_f = csv.reader(f)

for row in csv_f:
    for col in row:
        