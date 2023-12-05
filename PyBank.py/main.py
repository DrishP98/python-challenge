import os
import csv

#set file path
budget_data_csv = 'budget_data.csv'

#create lists
total_months = []
total_revenue = []
month_revenue_change = []
    
#open the CSV file 

with open(budget_data_csv) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    header = next(csvreader)

    #iterate through teh rows
    for row in csvreader:
         total_months.append(row[0])
         total_revenue.append(int(row[1]))

      #iterate through the profits to get through the monthly 

    for i in range(len(total_revenue)-1):

        # Take the difference between two months and append to monthly revenue change
         month_revenue_change.append(total_revenue[i+1]-total_revenue[i])

 # Max and min of the the montly revenue change list
max_increase_value = max(month_revenue_change)
max_decrease_value = min(month_revenue_change)
        
# Correlate max and min to the actual month with comparing with +1 as next month
max_increase_month = month_revenue_change.index(max(month_revenue_change)) + 1
max_decrease_month = month_revenue_change.index(min(month_revenue_change)) + 1 

# Print Statements asked for

print("Financial Analysis")
print("----------------------------")
print(f"total months: {len(total_months)}")
print(f"Total: ${sum(total_revenue)}")
print(f"Average Change: {round(sum(month_revenue_change)/len(month_revenue_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files to text
output_file = "Financial_Analysis_Summary.txt"

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"total months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_revenue)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(month_revenue_change)/len(month_revenue_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
    file.close()