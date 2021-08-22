# Open a file
fileHandle = open(file="my_file.txt")
# Read the contents of the file
contents = fileHandle.read()
# Print the contents
print(contents)
# Close the file
fileHandle.close()

# Another way to open a file, without worrying about closing it
with open(file="my_file.txt", mode="a") as fileHandle:
    fileHandle.write(" Hi!")

# Create a file if it doesn't exist. If it does, it will get overwritten
with open(file="new_file.txt", mode="w") as fileHandle:
    fileHandle.write(" Hi!")
