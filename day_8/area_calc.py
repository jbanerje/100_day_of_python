# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.

def cal_can_of_paints(height, width, coverage):
    no_of_cans = round((height * width) / coverage , 0)
    return no_of_cans


height = float(input('Enter Height : '))
width = float(input('Enter Width : '))
coverage = float(input('Enter Coverage : '))

print(f' No of cans needed is {cal_can_of_paints(height, width, coverage)}')
