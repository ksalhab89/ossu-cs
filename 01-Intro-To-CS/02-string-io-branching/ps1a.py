## 6.100A PSet 1: Part A
## Name: Khaled Salhab
## Time Spent:
## Collaborators:

import math

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################

yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

portion_down_payment = 0.25
amount_saved = 0
r = 0.05

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################

down_payment = portion_down_payment * cost_of_dream_home
monthly_saved = (yearly_salary / 12.0) * portion_saved
monthly_return = r / 12

months = math.log(1 + (monthly_return * (down_payment / monthly_saved))) / math.log(1 + monthly_return)
months = math.ceil(months)

print(f"Number of Months: {months}")
