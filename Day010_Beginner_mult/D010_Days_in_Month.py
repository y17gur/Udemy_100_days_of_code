def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# TODO: Add more code here 👇
def days_in_month(year_in, month_in):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year_in) and month_in == 2:
        return 29
    return month_days[month_in - 1]


# 🚨 Do NOT change any of the code below
year_input = int(input('year: '))  # Enter a year
month_input = int(input('month: '))  # Enter a month
days = days_in_month(year_input, month_input)
print(days)
