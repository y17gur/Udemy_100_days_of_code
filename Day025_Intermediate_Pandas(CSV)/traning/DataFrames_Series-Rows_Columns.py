# with open('weather_data.csv') as file:
#     data = file.readlines()
# print(data)

# import csv
#
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         try:
#             temperature.append(int(row[1]))
#         except:
#             pass
#
# print(temperature)

import pandas

data = pandas.read_csv('weather_data.csv')
data_dict = data.to_dict()

print(data_dict)

temp_list = data['temp'].to_list()
print(len(temp_list))

# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)

print(data['temp'].mean())
print(data['temp'].max())


# get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data['temp'].max()])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp * 9 / 5 + 32)

