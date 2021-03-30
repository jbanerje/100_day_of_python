# calculates the average student height from a List of heights
stu_height = input('Enter Student Height (use spce to seperate) - ').split()

sum_ht =0 
for s in stu_height:
    sum_ht += int(s)
print(f'Average Height of Class is {sum_ht/len(stu_height)}')