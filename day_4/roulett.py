# write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

import random

person = 'Angela, Ben, Jenny, Michael, Chloe'
person_list = person.split(',')
print(f'{person_list[random.randint(0, len(person_list))]} will pay the bill')

