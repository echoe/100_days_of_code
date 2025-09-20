WEATHER_DATA_FILE="weather_data.csv"
"""Let's go through csv and pandas real quick! Just different ways to read a csv file and such.
[Have I used the built-in CSV because of dependency issues on servers? So much ...]"""
# with open(WEATHER_DATA_FILE) as weather_data:
#     data = weather_data.readlines()
# print(data)
# import csv
# with open(WEATHER_DATA_FILE) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp": # This is a terrible way to do this, but it's the only real way I can see without using pandas haha.
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas

# data = pandas.read_csv(WEATHER_DATA_FILE)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == max(data.temp)])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print("Monday's temperature in F is ", (monday.temp[0] * 9/5 + 32))

# Create a dataframe from scratch

# data_dict_new = {
#     "students": ["Amy", "James", "Iris"],
#     "scores": [76, 56, 65]
# }
# data_new = pandas.DataFrame(data_dict_new)
# print(data_new)
# data_new.to_csv("new_data.csv")
SQUIRREL_CSV = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
data = pandas.read_csv(SQUIRREL_CSV)
data_dict_squirrel = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [sum(data["Primary Fur Color"] == "Gray"), sum(data["Primary Fur Color"] == "Cinnamon"), sum(data["Primary Fur Color"] == "Black")]
}
#The example used len() but it's functionally the same.
# print(sum(data["Primary Fur Color"] == "Gray"))
# print(sum(data["Primary Fur Color"] == "Cinnamon"))
# print(sum(data["Primary Fur Color"] == "Black"))
print(data_dict_squirrel)
data_squirrel = pandas.DataFrame(data_dict_squirrel)
data_squirrel.to_csv("smallsquirrel.csv")