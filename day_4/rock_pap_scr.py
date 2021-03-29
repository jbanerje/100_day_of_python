# Rock Paper Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice_map_pic = {0:rock, 1:paper, 2:scissors}
choice_map_var = {0:'Rock', 1:'Paper', 2:'Scissors'}

usr_choice = int(input('What do you chose ? Type 0 for Rock, 1 for Paper or 2 for Scissors - '))
print(f'You chose {choice_map_var[usr_choice]} {choice_map_pic[usr_choice]}')

comp_choice = random.randint(0, 2)
print(f'Computer chose {choice_map_var[comp_choice]} {choice_map_pic[comp_choice]}')


if usr_choice == 0 and comp_choice ==2 :
    print('You Win!')
elif comp_choice > usr_choice:
    print('Computer Win!')
elif comp_choice == usr_choice:
    print('Its a Tie!')
else:
    print('Invalid Option.You Loose!')