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

# Totals by candidate
total_votes = len(voter_id)
total_for_khan = len(khan_votes)
total_for_correy = len(correy_votes)
total_for_li = len(li_votes)
total_for_otooley = len(otooley_votes)

# Print statements
print(f"Election Results")
print(f"------------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------------")
print(f"Khan: {khans_percentage:.0%}({total_for_khan})")
print(f"Correy: {correys_percentage:.0%}({total_for_correy})")
print(f"Li: {lis_percentage:.0%}({total_for_li})")
print(f"O'Tooley: {otooleys_percentage:.0%}({total_for_otooley})")
print(f"------------------------")
print(f"Winner: {winner}")
print(f"------------------------")

# File output path
output_file = os.path.join('Analysis', 'Election_Results.txt')

with open(output_file, 'w',) as file:

# Write our data into Election_Results.txt
    file.write(f"Election Results\n")
    file.write(f"------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"------------------------\n")
    file.write(f"Kahn: {khans_percentage:..0%}({total_for_khan})\n")
    file.write(f"Correy: {correys_percentage:.0%}({total_for_correy})\n")
    file.write(f"Li: {lis_percentage:.0%}({total_for_li})\n")
    file.write(f"O'Tooley: {otooleys_percentage:.0%}({total_for_o'tooley})\n")
    file.write(f"------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write(f"------------------------\n")