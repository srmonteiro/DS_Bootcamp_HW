# Homework Assignment #3, Part 1: PyBank
# Brickey LeQuire 

#Import modules:
import os # file management
import csv # CSV read/write
import statistics # lies, damned lies, etc.

csvpath = os.path.join('Resources','budget_data.csv') # assign variable to path of input file

date = [] # month-year
pl = [] # monthly profit/loss for month in current row
pl_total = 0 # sum of all monthly profits/losses
pl_change = 0 # difference between current and previous monthly profit/loss
pl_change_list = [] # list of all pl_change values
pl_prev_row = 0 # profit/loss for month in previous row
months_total = 0 # total months in CSV data
avg_change = 0 # arithmetic mean of all pl_change values
max_increase = 0 # greatest month-to-month increase, in $
max_decrease = 0 # greatest month-t0-month decrease, in $
max_increase_month = () # month and year of max_increase
max_decrease_month = () # month and year of max_decrease
first_loop = True # set to false after first row of CSV file is read


with open(csvpath, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) # skip header row
    for row in csvreader: # loop through every row
        date.append(row[0]) # populate list of dates
        pl.append(row[1]) # populate list of profits/losses
        if first_loop == False: # once we've read two rows of data...
            pl_change = float(row[1]) - pl_prev_row # calculate difference between current month and previous
            pl_change_list.append(pl_change) # and store in a list
        pl_total = pl_total + float(row[1]) # keep running total of net profits/losses
        pl_prev_row = float(row[1]) # next month, this month's profit/loss will be last month's profit/loss
        if first_loop == True: # the first loop is followed by...
            first_loop = False # a bunch of not-first loops

months_total=len(date) # number of months in CSV file
avg_change = statistics.mean(pl_change_list) # caluclate average monthly change
max_increase = max(pl_change_list) # determine greatest monthly increase
max_decrease = min(pl_change_list) # determine greatest monthly decrease
max_increase_index = pl_change_list.index(max_increase) # get index number
max_decrease_index = pl_change_list.index(max_decrease)
max_increase_month = date[(max_increase_index+1)] # use index number to identify month/year
max_decrease_month = date[(max_decrease_index+1)] # (+1 because we don't have pl_change for first month)

# output results to screen
print()
print('Financial Analysis')
print('----------------------------')
print('Total Months: '+str(months_total))
print('Total: $'+'{:,.2f}'.format(pl_total))
print('Average Change: $'+'{:,.2f}'.format(avg_change))
print('Greatest Increase in Profits: $'+'{:,.2f}'.format(max_increase)+' ('+max_increase_month+')')
print('Greatest Decrease in Profits: $'+'{:,.2f}'.format(max_decrease)+' ('+max_decrease_month+')') 

# output results to text file
text_file = open("PyBank_output_PBL.txt", "w") # create text file in same folder as main.py, assign variable to path
text_file.write('Financial Analysis\n')
text_file.write('----------------------------\n')
text_file.write('Total Months: '+str(months_total)+'\n')
text_file.write('Total: $'+'{:,.2f}'.format(pl_total)+'\n')
text_file.write('Average Change: $'+'{:,.2f}'.format(avg_change)+'\n')
text_file.write('Greatest Increase in Profits: $'+'{:,.2f}'.format(max_increase)+' ('+max_increase_month+')\n')
text_file.write('Greatest Decrease in Profits: $'+'{:,.2f}'.format(max_decrease)+' ('+max_decrease_month+')\n') 
text_file.close() # if you open it, close it