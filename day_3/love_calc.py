# Love Calculator

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number #of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit #number.
# For Love Scores less than 10 or greater than 90 - you go together like coke and mentos
# For Love Scores between 40 and 50 - you are alright together
# Otherwise - you score is XXX

his_name = input('Enter his name :')
her_name = input('Enter her name :')

true_list = ['t', 'r', 'u', 'e']
love_list = ['l', 'o', 'v', 'e']

true_count = love_count = 0

his_and_her = (his_name + her_name).lower()
for letter in his_and_her:
    if letter in true_list:
        true_count += 1
    if letter in love_list:
        love_count += 1

final_score = int(str(true_count) + str(love_count))
print(final_score)

if (final_score < 10) or (final_score > 90):
    print(f'Your Score is {final_score}. You go together like Coke and Mentos')
elif (final_score >= 40) and (final_score <= 50):
    print(f'Your Score is {final_score}. You are alright together')
else:
    print(f'Your Score is {final_score}')