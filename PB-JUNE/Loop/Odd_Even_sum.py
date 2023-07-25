#Input
n = int(input())

#logic
sum1 = 0
sum2 = 0

for i in range(n):
    if i % 2 == 0:
        number = int(input())
        sum1 += number
    elif i % 2 != 0:
        number = int(input())
        sum2 += number

diff_sum1_sum2 = abs(sum1 - sum2)

#output
if sum1 == sum2:
    print('Yes')
    print(f'Sum = {sum1}')
if sum1 != sum2:
    print('No')
    print(f'Diff = {diff_sum1_sum2}')
