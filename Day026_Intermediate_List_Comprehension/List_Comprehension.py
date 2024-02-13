# List Comprehension

numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

list_range = [num*2 for num in range(1, 5)]
print(list_range)

# Conditional List Comprehension
names = ["Alex", "Beth", "Carol", "Dave", "Elena", "Fedor", "Camille"]

short_names = [name for name in names if len(name) < 5]
print(short_names)

upper_long_names = [name.upper() for name in names if len(name) >= 5]
print(upper_long_names)

# Task 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Your code below 👇
squared_numbers = [num * num for num in numbers]
# Your code above 👆
print(squared_numbers)
# Target Output
# [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]


# Task 2
imp = "9, 0, 32, 8, 2, 8, 64, 29, 42, 99"
list_of_strings = imp.split(',')
# 🚨 Do  not change the code above
print(list_of_strings)
# TODO: Use list comprehension to convert the strings to integers 👇:
list_of_int = [int(num) for num in list_of_strings]
print(list_of_int)
# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [num for num in list_of_int if num % 2 == 0]
# Write your code 👆 above:
print(result)
# Example Output
# [0, 32, 8, 2, 8, 64, 42]

# Task 3
with open("file1.txt") as data:
    list1 = [int(line.strip()) for line in data]

with open("file2.txt") as data:
    list2 = [int(line.strip()) for line in data]

result = [num1 for num1 in list1 if num1 in (num2 for num2 in list2)]

# Write your code above 👆
print(result)

# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
# e.g. if file1.txt contained:
# 1
# 2
# 3
# and file2.txt contained:
# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT: The output should be a list of integers and not strings! Try to use List Comprehension instead of a Loop.

# Example Output
# [3, 6, 5, 33, 12, 7, 42, 13]


