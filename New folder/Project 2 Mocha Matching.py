import pandas as pd
import csv
import random
import copy
import os

# path to the CSV files with participant data
participants_csv = "Coffee Partner Lottery participants.csv"

# header names in the CSV file (name, e-mail and cat or dog person of participants)
header_name = "Name"
header_email = "E-mail"
header_animal = "Are you a dog person or a cat person?"

# path to CSV file that stores the pairings of this round
new_pairs_csv = "Coffee Partner Lottery new pairs.csv"

# path to CSV file that stores all pairings (to avoid repetition)
all_pairs_csv = "Coffee Partner Lottery all pairs.csv"

# load participant's data
formdata = pd.read_csv(participants_csv)

# create list of participants
participants = list(set(formdata[header_name]))

# init list of old pairs
opairs = []

DELIMITER = ','

# load all previous pairings (to avoid redundancies)
if os.path.exists(all_pairs_csv):
    with open(all_pairs_csv, "r") as file:
        csvreader = csv.reader(file, delimiter=DELIMITER)
        for row in csvreader:
            group = []
            for i in range(0, len(row)):
                group.append(row[i])
            opairs.append(tuple(group))

# init list of new pairs
npairs = []

# Make copy of list of participants
nparticipants = copy.deepcopy(participants)

# Make separate lists of participants for dog lovers and cat lovers
dog_lovers = formdata[formdata[header_animal] == "Dog"][header_email].tolist()  # use header_email instead of header_name
cat_lovers = formdata[formdata[header_animal] == "Cat"][header_email].tolist()  # use header_email instead of header_name

# Shuffle the lists of participants
random.shuffle(dog_lovers)
random.shuffle(cat_lovers)

# Create groups with 2 to 5 participants from each list
while dog_lovers:
    group_size = min(5, len(dog_lovers))
    if group_size < 2:
        group_size = 2
    group = []
    for i in range(group_size):
        participant = dog_lovers.pop()
        group.append(participant)
    if len(group) % 2 == 1:  # if group size is odd, remove one participant and create a new group
        extra_participant = group.pop()
        if dog_lovers:  # check if there are still participants left in the list
            extra_group = [extra_participant, dog_lovers.pop()]
            if set(extra_group).isdisjoint(opairs):
                npairs.append(extra_group)
                opairs.append(tuple(extra_group))
    group.sort()
    if set(group).isdisjoint(opairs):
        npairs.append(group)
        opairs.append(tuple(group))

while cat_lovers:
    group_size = min(5, len(cat_lovers))
    if group_size < 2:
        group_size = 2
    group = []
    for i in range(group_size):
        participant = cat_lovers.pop()
        group.append(participant)
    if len(group) % 2 == 1:  # if group size is odd, remove one participant and create a new group
        extra_participant = group.pop()
        if cat_lovers:  # check if there are still participants left in the list
            extra_group = [extra_participant, cat_lovers.pop()]
            if set(extra_group).isdisjoint(opairs):
                npairs.append(extra_group)
                opairs.append(tuple(extra_group))
    group.sort()
    if set(group).isdisjoint(opairs):
        npairs.append(group)
        opairs.append(tuple(group))


# Write new pairs to CSV file
with open(new_pairs_csv, "w", newline='') as file:
    csvwriter = csv.writer(file, delimiter=DELIMITER)
    for group in npairs:
        csvwriter.writerow(group)

# Write all pairs to CSV file
with open(all_pairs_csv, "w", newline='') as file:
    csvwriter = csv.writer(file, delimiter=DELIMITER)
    for group in opairs:
        csvwriter.writerow(group)

#########
with open("convo_starters.csv", "r") as file:
    reader = csv.reader(file)
    data_list = list(reader)

with open("Coffee Partner Lottery new pairs.csv", "r") as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Skip the header row
    next(csv_reader)

    # Iterate over the participant names and print the message for each one
    for row in csv_reader:
        convo_starter = random.choice(data_list)
        pair = row
        message = f"Dear {', '.join([formdata[formdata[header_email] == p].iloc[0][header_name] for p in pair])},\n\nWe would love to inform you that you have been matched for a meeting with a coffee partner! You can start your conversation with \n\n{convo_starter}\n\nGood luck."
        print(message)
        print("------------------------")

        # append message to output string
output_string = ""
output_string += message + "\n\n"

# assemble output for printout
output_string = ""
output_string += "Today's coffee partners:\n"
output_string += "------------------------\n"

for pair in npairs:
    pair = list(pair)
    output_string += "* "
    for i in range(0, len(pair)):
        name_email_pair = f"{formdata[formdata[header_email] == pair[i]].iloc[0][header_name]} ({pair[i]})"
        if i < len(pair) - 1:
            output_string += name_email_pair + ", "
        else:
            output_string += name_email_pair
    output_string += "\n"

# print the output
print(output_string)



messages = []
for pair in npairs:
    convo_starter = random.choice(data_list)
    message = f"Dear {', '.join([formdata[formdata[header_email] == p].iloc[0][header_name] for p in pair])},\n\nWe would love to inform you that you have been matched for a meeting with a coffee partner! You can start your conversation with \n\n{convo_starter}\n\nGood luck."
    messages.append(message)

# Save the messages to a file
# with open(#fill in own directionary, "w" as file:
#     file.write("\n".join(messages))
    
# print("Messages are saved to file: Message_file.txt")
