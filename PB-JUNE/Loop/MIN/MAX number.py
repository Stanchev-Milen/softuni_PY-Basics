#Input
n = int(input())

#Logic
for i in range(n):
    if i == 0:
        min_value = int(input())
        max_value = min_value
    if i != 0:
        number = int(input())
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number

#Output

print(f'Max number: {max_value}')
print(f'Min number: {min_value}')
