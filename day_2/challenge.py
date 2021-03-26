# Given your age as input calcuate how many days, weeks and year you have to live till you are 90.
# Assumptions - 365 days, 12 months, 52 weeks and 7 days
# Round all details.

current_age = int(input('What is your current age ? '))
years_to_live = (90 - current_age)
print(f'You have {years_to_live} years\n {years_to_live * 12} months \n {years_to_live * 52 } weeks \n {years_to_live * 365} days')

