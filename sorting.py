numbers = [3, 7, 4, 8, 35, 2, 7, 2, 78, 3, 32, 1, 6, 8, 9, 0, 6, 3, 6, 8]
numbers.sort()
print(numbers)


unique_number = set(numbers)
print(unique_number)
sorted_numbers = sorted(unique_number)
print(sorted_numbers)
reverse_no = sorted("Reveers No", unique_number, reverse=True)
print(reverse_no)
