import csv
with open('output.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Print each row of the CSV file