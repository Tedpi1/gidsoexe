user_input=[]
for i in range(5):
    num = int(input("Enter a number: "))
    user_input.append(num)
    print("Input List:", user_input)
total=sum(user_input)
print("Total:", total)
average=total/len(user_input)
print("Average:", average)