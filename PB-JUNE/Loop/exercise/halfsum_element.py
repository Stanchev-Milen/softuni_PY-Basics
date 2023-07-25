#input
n = int(input())

#logic
max_element = int(input())
sum = max_element

for i in range(n - 1):
    number = int(input())
    if max_element < number:
        max_element = number
    sum += number


sum_without_max_element = abs(sum - max_element)

diff_numbers_max_element = abs(sum_without_max_element - max_element)
#output

if diff_numbers_max_element == 0:
    print(f'Yes')
    print(f'Sum = {max_element}')
elif diff_numbers_max_element != 0:
    print('No')
    print(f'Diff = {diff_numbers_max_element}')