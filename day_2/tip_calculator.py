# Tip Calculator

print("Welcome to Tip Calculator!")

total_bill = float(input('What is your total bill in $ ? '))
tip        = int(input('What percentage of tip would you like to pay ? 10, 12 or 15 ? '))
people_count = int(input('How many people to split the bill ? '))

ind_contribution = (total_bill + (total_bill*(tip/100)))/people_count

print(f'Each person should pay - ${round(ind_contribution, 2)}')
