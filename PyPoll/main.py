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
