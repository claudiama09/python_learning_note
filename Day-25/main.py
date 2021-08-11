# 1) Pure python code
# data = []
#
# with open('./weather_data.csv') as weather_data:
#     for weather in weather_data:
#         data.append(weather.strip())
#
# print(data)

# 2) Use python csv library
# -----------------------------------------------------------
# import csv
#
# with open('./weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# 3) Use python pandas library
# -----------------------------------------------------------
import pandas

data = pandas.read_csv('weather_data.csv')
# print(data)
print(data['temp'])
