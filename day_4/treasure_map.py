# Treasure Map . Write a program which will mark a spot with an X and simulate a co-ordinate

row_1 = ['?', '?', '?']
row_2 = ['?', '?', '?']
row_3 = ['?', '?', '?']

full_board = [row_1, row_2, row_3]
print(f'{row_1}\n{row_2}\n{row_3}')

usr_inp = str(input('Which row, column you want to update (example- 00, 01) ? '))
usr_sel = [int(i) for i in usr_inp]

full_board[usr_sel[0]][usr_sel[1]] = 'X'

print(f'{full_board[0]}\n{full_board[1]}\n{full_board[2]}')
