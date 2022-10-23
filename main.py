# Income Tax Calculator
# Refer to README.md for directions followed to complete income calculator

#All taxpayers are charged a flat tax rate of 20%
tax_rate = 0.20

#All taxpayers are allowed a $10,000 standard deduction
standard_deduction = 10000

#Gross income - Gross income is entered using an input variable
gross_income = float(input("Enter the gross income: "))

#Number of dependents - Number of dependts is entered using an input variable
number_of_dependents = int(input("Enter the number of dependents: "))

#For each dependent, a taxpayer is allowed an additional $3,000 deduction
if number_of_dependents >= 0:
    additional_deduction = number_of_dependents * 3000
    
# Calculating Income Tax
income_tax = (gross_income - standard_deduction - (additional_deduction)) * tax_rate

#Output
print("The income tax is", income_tax)