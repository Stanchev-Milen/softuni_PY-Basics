reference_num = int(input())
is_happy = False

for i in range(1, 9 + 1):
    for j in range(1, 9 + 1):
        for k in range(1, 9 + 1):
            for l in range(1, 9 + 1):

                sum_first_two = j + i
                sum_latter_two = k + l
                if sum_first_two == sum_latter_two:
                    is_happy = True

                if is_happy:
                    if not reference_num % sum_first_two == 0:
                        is_happy = False
                if is_happy:
                    print(f'{i}{j}{k}{l}', end=' ')
                sum_first_two = 0
                sum_latter_two = 0
                is_happy = False
