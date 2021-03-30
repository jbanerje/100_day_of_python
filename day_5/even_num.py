# Add Even Number from 1 to 100
sum_even_num = 0
for num in range(1, 101):
    if num%2 == 0:
        sum_even_num += num
print(sum_even_num)