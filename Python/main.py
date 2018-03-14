import os
import csv

# Path to collect data from the Assignments folder
budgetdata_csv = os.path.join('..','myPython','budget_data_1.csv')

  month = [0]
  total_revenue = [0]
  increased_value = ["", + 0]:
  decreased_value = ["", + 0]:
 
  for row in csvreader:
      #print(row[1])
      month += 1
      if month != 1:
          total_revenue = total_revenue + int(row[1])
          if lastmonth_value != 0 and (increased_value[1] < int(row[1]) - lastmonth_value[1]):
              increased_value[0] = row [0]
              increased_value[1] = int(row[1]) -lastmonth_value[1]
              #print("Value Increased: " + str(increased_value[1]))
         
          # print(row[0])
          if lastmonth_value != 0 and (decreased_value[1] > int(row[1]) - lastmonth_value[1]):
              decreased_value[0] = row[0]
              decreased_value[1] = int(row[1]) - lastmonth_value[1]
              #print("Value Decreased: " + str(decreased_value[1]))
          lastmonth_value[1] = int(row[1])
          lastmonth_value[0] = row[0]
          
    # Print out the total months, total revenue, avereage revenue change and greatest increase in revenue
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months: " + str(month - 1))
    print("Total Revenue: $" + str(total_revenue))
    print("Average Revenue Change: $" + str(total_revenue / (month -1)))
    print("Greatest Increase in Revenue: " + str(increased_value))
    print("Greatest Decrease in Revenue: " + str(decreased_value)

#with open(Data_1, newline="", encoding='latin-1') as csvfile:
with open(budgetdata_csv, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
    