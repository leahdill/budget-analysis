import os
import csv

# State working data location
csvpath=os.path.join("Resources","budget_data.csv")
 
# Open csv
with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",") 
    # Skip the header to grab data
    csv_header = next(csvreader) 

    # Declare datasets to assign data and further analyze
    months = []
    profits = []
    monthly_profit_difference = [] 

    # Scan through the rows of the csv file to pull data
    for row in csvreader: 

        # Append the months and profits to their assigned dataset
        months.append(row[0])
        profits.append(int(row[1]))

    # Scan the profits to find changes
    for i in range(len(profits)-1):
        monthly_profit_difference.append(profits[i+1]-profits[i])
        
# Find the max and min of the profits
max_value_increase = max(monthly_profit_difference)
max_value_decrease = min(monthly_profit_difference)

max_monthly_increase = monthly_profit_difference.index(max(monthly_profit_difference)) + 1
max_monthly_decrease = monthly_profit_difference.index(min(monthly_profit_difference)) + 1 

# Print statements

print("Financial Analysis")
print("------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profits)}")
print(f"Average Change: {round(sum(monthly_profit_difference)/len(monthly_profit_difference),2)}")
print(f"Greatest Increase in Profits: {months[max_monthly_increase]} (${(str(max_value_increase))})")
print(f"Greatest Decrease in Profits: {months[max_monthly_decrease]} (${(str(max_value_decrease))})")

# File output path
output_file = os.path.join("analysis","Financial_Analysis.txt")

with open(output_file,"w") as file:
    
# Write our data into Financial_Analysis.txt
    file.write("Financial Analysis")
    file.write("\n")
    file.write("------------------")
    file.write("\n")
    file.write(f"Total Months: {len(months)}")
    file.write("\n")
    file.write(f"Total: ${sum(profits)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_difference)/len(monthly_profit_difference),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {months[max_monthly_increase]} (${(str(max_value_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {months[max_monthly_decrease]} (${(str(max_value_decrease))})")