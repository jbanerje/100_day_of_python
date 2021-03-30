# FizzBuzz Game
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# If the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`
fifteen_flag = 'N'
for num in range(1, 101):
    
    if num%15 == 0:
        print('Fizzbuzz!')
        fifteen_flag = 'Y'
    
    if fifteen_flag == 'N':
        if num%5 == 0:
            print('Buzz!')
        elif num%3 == 0:
            print('Fizz!')
        else:
            print(num)
    
    fifteen_flag = 'N'