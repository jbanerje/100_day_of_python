import art
import random

def play_game(chances):
    
    game_number = random.randint(1, 100)
    print(game_number)
    
    for i in range(0, chances):
        user_input = int(input('Guess Your Number : '))
        if user_input < game_number    :
            print('Too Low! Guess Again!')
        elif user_input > game_number    :
            print('Too High! Guess Again!')
        else:
            print('Awesome Guess! You Win!')
            break
    print('Game Over!')
    return


if __name__ == '__main__':
    print(art.logo)

    player_level = int(input('\n Welcome to the Number Guessing Game! \n I am thinking of a number between 1 and 100 \n Choose your difficulty level - Easy (0) and Hard(1) : '))

    if player_level == 0 :
        play_game(10)
    elif player_level == 1 :
        play_game(5)
    else:
        print('Incorrect Choice! Game Over!') 

