PLACEHOLDER = "[name]"

# Get the names of the people to be invited
with open(file="./Input/Names/invited_names.txt") as name_file:
    people = name_file.readlines()

# Get the template for the letter
with open(file="./Input/Letters/starting_letter.txt") as starting_letter:
    letter_template = starting_letter.read()

# for each name in invited_names.txt
for name in people:
    # Replace the [name] placeholder with the actual name.
    invitation_letter = letter_template.replace(PLACEHOLDER, name.strip())

    # Save the letters in the folder "ReadyToSend".
    with open(file=f"./Output/ReadyToSend/{name}.txt", mode="w") as invitation_file:
        invitation_file.write(invitation_letter)
