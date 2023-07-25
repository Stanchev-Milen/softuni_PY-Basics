smaller_num = int(input())
bigger_num = int(input())

#Lo

for current_num in range(smaller_num, bigger_num + 1):
    num_to_string = str(current_num)
    sum_even = 0
    sum_odd = 0

    for position in range(len(num_to_string)):

        if position % 2 == 0:
            number_to_sum_odd = int(num_to_string[position])
            sum_odd += number_to_sum_odd
        elif position % 2 != 0:
            number_to_sum_even = int(num_to_string[position])
            sum_even += number_to_sum_even

    if sum_odd == sum_even:
        print(current_num, end=' ')
