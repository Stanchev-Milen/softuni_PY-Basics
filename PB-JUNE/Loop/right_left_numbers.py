#Input
n = int(input())

#Logic
sum1 = 0
sum2 = 0

for i in range(n):
    number = int(input())
    sum1 += number
for i in range(n):
    number = int(input())
    sum2 += number

diff_sum1_sum2 = abs(sum1 - sum2)

if sum1 == sum2:
    print(f'Yes, sum = {sum1}')
if sum1 != sum2:
    print(f'No, diff = {diff_sum1_sum2}')

#Output
