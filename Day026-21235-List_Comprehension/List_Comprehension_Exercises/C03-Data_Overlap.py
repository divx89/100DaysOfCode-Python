with open("file1.txt") as file1:
    num_list1 = file1.readlines()

with open("file2.txt") as file2:
    num_list = [int(num) for num in file2.readlines() if num in num_list1]

print(num_list1)
print(num_list)
