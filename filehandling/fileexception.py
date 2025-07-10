try:
    with open('output.csv', mode='r') as file:
        print(file.read())
except FileNotFoundError as e:
    print("File not found:")

try:
    with open('tad.csv', mode='w') as file:
        file.write("This is a test file.")
        print("File written successfully.")
except IOError as e:
    print("Permission denied:", e)