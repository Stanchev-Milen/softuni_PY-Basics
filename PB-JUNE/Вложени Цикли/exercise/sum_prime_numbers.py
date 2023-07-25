current_number = (input())
sum_all_prime = 0
sum_all_not_prime = 0

while current_number != 'stop':
    current_number = int(current_number)
    if current_number < 0:
        print('Number is negative.')
    else:
        is_prime = True
        for i in range(2, current_number):
            if current_number % i == 0:
                is_prime = False
                break
        if not is_prime:
            sum_all_not_prime += current_number
        else:
            sum_all_prime += current_number

    current_number = input()

print(f'Sum of all prime numbers is: {sum_all_prime}')
print(f"Sum of all non prime numbers is: {sum_all_not_prime}")

