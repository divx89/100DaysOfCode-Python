# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
try:
  number = int(position)
  if number < 11 or number > 33:
    raise ValueError
  row = number % 10 - 1
  column = number // 10 - 1

  map[row][column] = "X"
  print(f"{row1}\n{row2}\n{row3}")
except ValueError:
  print("Incorrect input value")