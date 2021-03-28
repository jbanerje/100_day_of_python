# Code to determine whether a year is a leap year
# To determine whether a year is a leap year, follow these steps:
    # 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
    # 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
    # 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
    # 4. The year is a leap year (it has 366 days).
    # 5. The year is not a leap year (it has 365 days).

user_year = int(input('Provide a year for leap year check - '))

if user_year % 4 != 0:
    print('Not a leap year')
else:
    if user_year % 100 != 0:
        print('Leap Year!')
    else:
        if user_year % 400 == 0:
            print('Leap Year')
        else:
            print('Not a Leap Year')
