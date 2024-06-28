import csv
import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"])

data_dict = {"Fur Color": ["Gray", "Cinnamon", "Black"], "Count": []}

gray_count = 0
red_count = 0
black_count = 0


for fur_color in data["Primary Fur Color"]:
    if fur_color == "Gray":
        gray_count += 1
    elif fur_color == "Cinnamon":
        red_count += 1
    elif fur_color == "Black":
        black_count += 1

data_dict["Count"].insert(0, gray_count)
data_dict["Count"].insert(1, red_count)
data_dict["Count"].insert(2, black_count)


df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
print(data_dict)
