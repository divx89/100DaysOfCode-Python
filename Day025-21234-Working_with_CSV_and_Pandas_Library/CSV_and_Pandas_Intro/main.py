# import csv
import pandas

# Extract data without csv library
# weather_data = []
# with open(file="./weather_data.csv") as weather_file:
#     while line := weather_file.readline():
#         weather_data.append(line[:-1].split(","))
# print(weather_data)

# Extract data using the csv library
# with open(file="./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

# Extract using pandas
data = pandas.read_csv("./weather_data.csv")

# Converting the extracted data into a dictionary
# data_dict = data.to_dict()
# print(data_dict)

# Extracting the data of a single column into a list
temp_list = data["temp"].to_list()
print(temp_list)

# Doing computations on extracted data manually
# avg_temp = round(sum(temp_list)/len(temp_list), 2)
# print(f"Average temperature is {avg_temp}")

# Doing computations on extracted data using pandas methods
print(f'The average temperature was {round(data["temp"].mean(), 2)}')
print(f'The maximum temperature was {data["temp"].max()}')

# Extracting column data without the square bracket notation
print(data.condition)

# Extract data from a row (say, Monday)
print("Data for Monday")
monday = data[data.day == "Monday"]
print(monday, "\n")
print("Temperature on Monday")
print(int(monday.temp) * (9 / 5) + 32, "deg. F\n")

print("Data for the day with the max temperature")
print(data[data.temp == data.temp.max()])

#############################################################
# Create a dataframe from scratch
data_dict = {"students": ["Amy", "James", "Angela"],
             "scores": [76, 56, 65]
             }

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_data_frame.csv")
