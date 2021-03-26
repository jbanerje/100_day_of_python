# Ex-1 : Calculate sum of 2 digit number
user_input = int(input('Please provide a 2 digit number:'))
sum_input = user_input%10 + user_input//10
print('Sum of digit is {}'.format(sum_input))
print(f"Sum of digit is {sum_input}")

# # Calculate BMI
height = input('Please provide height:')
weight = input('Please provide weight:')

print('BMI-{}'.format(round(float(weight)/(float(height) ** 2)), 2))


