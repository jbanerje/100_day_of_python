# Prime Number Checker

def prime_num_check(num):
    counter = 0
    
    for i in range(1, num+1):
        if num % i == 0:
            counter += 1
        if counter > 2:
            break
    
    if counter <= 1:
        print('Neither prime Nor Composit')
    elif counter == 2:
        print('Prime Number')
    else:
        print('Composit Number')


num = int(input("Enter a number for prime Check: "))
prime_num_check(num)