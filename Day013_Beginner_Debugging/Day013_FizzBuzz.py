target = int(input())

for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:  # was or
        print("FizzBuzz")
    elif number % 3 == 0:  # was if
        print("Fizz")
    elif number % 5 == 0:  # was if
        print("Buzz")
    else:
        print(number)
