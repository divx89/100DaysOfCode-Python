import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = {}
for color in data["Primary Fur Color"].dropna():
    colors[color] = colors.get(color, 0) + 1

colors_dict = {"Fur Color": list(colors.keys()),
               "Number of Squirrels": list(colors.values())}

squirrel_frame = pandas.DataFrame(colors_dict)
squirrel_frame.to_csv("squirrel_count.csv")
