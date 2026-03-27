import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260327.csv")

# print(data["Primary Fur Color"])

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_dict ={
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")