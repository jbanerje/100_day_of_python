# pogram to calculate the bmi indicator

weight = float(input('What is your weight (kg)? '))
height = float(input('What is your height (m)? '))

bmi = int(round(weight/(height**2),0))

if bmi < 18.5:
    print('Your bmi index is {bmi} . You are underweight')
elif bmi >= 18.5 and bmi < 25:
    print('Your bmi index is {bmi} . You are normal weight')
elif bmi >= 25 and bmi < 30:
    print('Your bmi index is {bmi} . You are slighly over weight')
elif bmi >= 30 and bmi < 35:
    print('Your bmi index is {bmi} . You are obese')
else:
    print('Your bmi index is {bmi} . You are clinically Obese')