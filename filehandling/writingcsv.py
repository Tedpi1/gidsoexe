import csv

data= [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Alice", 25, "Los Angeles"],
]

with open('output.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerows(data)
