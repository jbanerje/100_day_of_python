# Hangman Game

import random
import hangman_art
import hangman_words

# Defining the constants
word=""
counter = 0
match = 'n'
chnce_rem = 6

# Main program
if __name__ =='__main__':


    print(hangman_art.logo)

    usr_guess_word = random.choice(hangman_words.word_list)
    
    # print(usr_guess_word)
      
    print(f'Its a {len(usr_guess_word)} letter word. Guess what it is ?')
    
    # Create Blanks
    letter_list = ['_'] * len(usr_guess_word)
    print(letter_list)

    # Run  the loop till user makes 7 mistakes and there is still a blank position
    while '_' in letter_list and chnce_rem >= 0:
        usr_letter = input('\nEnter a letter - ').lower()
        
        # User guesed it Correct
        for letter in usr_guess_word:
            if usr_letter == letter:
                letter_list[counter] = usr_letter
                match='y'
            counter += 1
        
        # User Guessed it wrong
        if match == 'n':
            print(hangman_art.stages[chnce_rem])
            chnce_rem = chnce_rem - 1

        # Resetting the constant flags
        counter=0
        match='n'

        # Display the after results of user input
        print(letter_list)
        final_list = letter_list
    
    #Check if user has got all letters.
    if '_' in final_list:
        print('Game Over!')
    else:
        print('You Won!')