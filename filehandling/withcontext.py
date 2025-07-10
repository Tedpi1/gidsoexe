with open('gidso.txt', 'w') as file:
    file.write('We are now Working With with Context\n')
with open('gidso.txt', 'r') as file:
    content = file.read()
    print(content)  
    