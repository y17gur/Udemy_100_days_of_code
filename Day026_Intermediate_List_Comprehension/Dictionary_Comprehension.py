import random

names = ["Alex", "Beth", "Carol", "Dave", "Elena", "Fedor", "Camille"]
students_score = {student: random.randint(1, 100) for student in names}
print(students_score)

passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
print(passed_students)


# Dictionary Comprehension 1

# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given
# sentence and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words.
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

# Example Input
# What is the Airspeed Velocity of an Unladen Swallow?
# Example Output
# {
# 'What': 4,
# 'is': 2,
# 'the': 3,
# 'Airspeed': 8,
# 'Velocity': 8,
# 'of': 2,
# 'an': 2,
# 'Unladen': 7,
# 'Swallow?': 8
# }
#

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# 🚨 Don't change code above 👆
# Write your code below 👇
result = {word: len(word) for word in sentence.split()}
print(result)


# Dictionary Comprehension 2

# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in
# degrees Celsius and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f use this formula:
# (temp_c * 9/5) + 32 = temp_f

# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
# The eval() function will help us convert the string input into a Python dictionary, provided that the inputs are
# already formatted with the correct syntax.

# Example Input
# {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# Example Output
# {'Monday': 53.6,
# 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# 🚨 Don't change code above 👆
weather_f = {day: ((temp * 9/5) + 32) for (day, temp) in weather_c.items()}
# Write your code 👇 below:

print(weather_f)
