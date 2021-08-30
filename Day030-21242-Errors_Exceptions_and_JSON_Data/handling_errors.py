# -------------------------------------------- #
#             Common Errors
# -------------------------------------------- #
# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# Index Error
# fruit_list = ["apple", "banana"]
# fruit = fruit_list[2]

# TypeError
# x = 10
# y = x[1]

# -------------------------------------------- #
#             Exception Handling
# -------------------------------------------- #

try:
    file = open("a_file.txt")
except FileNotFoundError as error_message:
    print(error_message, "; Creating it instead")
    file = open("a_file.txt", "w")
    file.write("Something")
else:
    content = file.read()
    print(content)
finally:
    file.close()

try:
    a_dictionary = {"key": "value"}
    print(a_dictionary["some_key"])
except KeyError as error_message:
    print(f"The key {error_message} does not exist")

height = float(input("Enter Height in m: "))
weight = float(input("Enter weight in kg: "))

if height > 2.5:
    raise ValueError("Human heights should not be over 2.5 m")

bmi = weight / height**2
print(bmi)