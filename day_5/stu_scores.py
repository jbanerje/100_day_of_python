# calculates the highest score from a List of scores
stu_scores = input('Enter Student scores (use spce to seperate) - ').split()

grt_num = 0 

for s in stu_scores:
    if int(s) > grt_num:
        grt_num = int(s)
print(f'Greatest number is {grt_num}')