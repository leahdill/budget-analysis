import csv
import os

#State working data location
csvpath=os.path.join("Resources", "election_data.csv")

# Open csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header to grab data
    csv_header = next(csvreader)

    #Declare lists
    voter_id = []
    county = []
    name = []
    khan_votes = []
    correy_votes = []
    li_votes =[]
    otooley_votes = []

    # Loop through the data
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        name.append(row[2])

        row_count = 0
        row_count = row_count + 1

    # Append candidate names to their dataset
        if (row[2] == "Khan"):
            khan_votes.append(row[2])
        elif (row[2] == "Correy"):
            correy_votes.append(row[2])
        elif (row[2] == "Li"):
            li_votes.append(row[2])
        else:
            otooley_votes.append(row[2])

# Totals and per candidate
total_votes = len(voter_id)
total_for_khan = len(khan_votes)
total_for_correy = len(correy_votes)
total_for_li = len(li_votes)
total_for_otooley = len(otooley_votes)

# Get each candidate's percentage of the total votes
khans_percentage = total_for_khan / total_votes
correys_percentage = total_for_correy / total_votes
lis_percentage = total_for_li / total_votes
otooleys_percentage = total_for_otooley / total_votes

# Determinations for winner
if total_for_khan > total_for_correy and total_for_li and total_for_otooley:
    winner = "Khan"
elif total_for_correy > total_for_khan and total_for_li and total_for_otooley:
    winner = "Correy"
elif total_for_li > total_for_khan and total_for_correy and total_for_otooley:
    winner = "Li"
else:
    winner = "O'Tooley"

# Print statements
# Note to grader: I understand that noting .0% will output no decimal places in my percentage, thus not giving an identical result to our example, 
# but it physically hurts to look at an output with three useless zeroes at the end. Hopefully this simplified output is acceptable!
print(f"Election Results")
print(f"---------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------")
print(f"Khan: {khans_percentage:.0%}({total_for_khan})")
print(f"Correy: {correys_percentage:.0%}({total_for_correy})")
print(f"Li: {lis_percentage:.0%}({total_for_li})")
print(f"O'Tooley: {otooleys_percentage:.0%}({total_for_otooley})")
print(f"---------------------")
print(f"Winner: {winner}")
print(f"---------------------")

# File output path
output_file = os.path.join('Analysis', 'Election_Results.txt')

with open(output_file, 'w',) as file:

# Write our data into Election_Results.txt
    file.write(f"Election Results\n")
    file.write(f"---------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"---------------------\n")
    file.write(f"Kahn: {khans_percentage:.0%}({total_for_khan})\n")
    file.write(f"Correy: {correys_percentage:.0%}({total_for_correy})\n")
    file.write(f"Li: {lis_percentage:.0%}({total_for_li})\n")
    file.write(f"O'Tooley: {otooleys_percentage:.0%}({total_for_otooley})\n")
    file.write(f"---------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write(f"---------------------\n")