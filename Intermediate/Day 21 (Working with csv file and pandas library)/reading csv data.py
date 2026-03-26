# with open("2. weather_data.csv") as file:
#     data = file.readlines()
#     print(data)


# import csv
#
# with open("2. weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempratures = []
#     for row in data:
#         if row[1] != "temp":
#             tempratures.append(int(row[1]))
#     print(tempratures)

import pandas as pd

data = pd.read_csv("2. weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data["temp"]))

#
# data_list=data["temp"].tolist()
# print(data_list)

# calculate average temprature
# sum=0
# for num in data_list:
#     sum += num
# avg=sum/len(data_list)
# print(avg)

# second method
# avg = sum(data_list) / len(data_list)
# print(avg)
#
# maxi = max(data_list)
# print(maxi)
#
# print(data[data.temp == data.temp.max()])


# Get data in row
print(data[data.day == "Monday"])

data_dict = data.to_dict()
# print(data_dict)

fahrenheit = []
for da in data["temp"]:
    fah = int(da * (9 / 5) + 32)
    fahrenheit.append(fah)

# print(fahrenheit)

df = pd.DataFrame(data_dict)
df = df.assign(fahrenheit=[53, 57, 59, 57, 69, 71, 75])

print(df)
df.to_csv("updated data.csv")
