# Build a Calculator using Fucntions and Dictionaries

import art

def add_num(num1, num2):
    return num1 + num2

def sub_num(num1, num2):
    return num1 - num2

def multiply_num(num1, num2):
    return num1 * num2

def divide_num(num1, num2):
    return float(num1 / num2)


if __name__ == "__main__":

    want_to_cont = 'y'

    print(art.logo)
    
    num1 = float(input('Enter First Number : '))
    
    while want_to_cont != 'n':
        num2 = float(input('Enter Next Number : '))

        math_operations = { '+' : add_num(num1, num2),
                            '-' : sub_num(num1, num2),
                            '*' : multiply_num(num1, num2),
                            '/' : divide_num(num1, num2)}

        print('Operations available are :')
        for keys in math_operations:
            print(keys)
        
        operation = input('Choose a math operation : ')
        print(f'Result - {math_operations[operation]}')
        num1 = math_operations[operation]

        want_to_cont = input('Want to Continue (y/n) ? : ').lower()
    
    print('Thanks for using the calculator!')
    