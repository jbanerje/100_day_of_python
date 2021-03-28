# Based on a user's order, work out their final bill.

# Base Price
pizza_size_dict = {'S':15, 'M':20, 'L':25}

# Pepproni price
pizza_size = input('What size Pizza would you like (S/M/L) ? ')
pepproni = input('Would you like Pepperoni (Y/N) ?')

if pepproni == 'Y' or pepproni == 'y':
    print(f'Your final price is ${pizza_size_dict[pizza_size] + 2}')
elif pepproni == 'N' or pepproni == 'n':
    print(f'Your final price is ${pizza_size_dict[pizza_size]}')
else:
    print('Incorrect Pepproni Requirments')
