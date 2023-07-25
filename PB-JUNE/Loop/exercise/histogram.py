#Input
n = int(input())

#Logic
sum_num_smaller_than_200 = 0
sum_num_200_399 = 0
sum_num_400_599 = 0
sum_num_600_799 = 0
sum_num_bigger_than_800 = 0

for i in range(n):
    number = int(input())
    if number < 200:
        sum_num_smaller_than_200 += 1
    elif 200 <= number <= 399:
        sum_num_200_399 += 1
    elif 400 <= number <= 599:
        sum_num_400_599 += 1
    elif 600 <= number <= 799:
        sum_num_600_799 += 1
    elif number >= 800:
        sum_num_bigger_than_800 += 1
p1 = 100 * (sum_num_smaller_than_200 / n)
p2 = 100 * (sum_num_200_399 / n)
p3 = 100 * (sum_num_400_599 / n)
p4 = 100 * (sum_num_600_799 / n)
p5 = 100 * (sum_num_bigger_than_800 / n)

#output
print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')