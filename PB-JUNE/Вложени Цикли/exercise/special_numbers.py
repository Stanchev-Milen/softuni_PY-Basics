n = int(input())

for i in range(1111, 9999 + 1):
    i_to_string = str(i)
    all_fine = True

    for j in range(len(i_to_string)):
        digit_to_check = int(i_to_string[j])

        if digit_to_check != 0 and n % digit_to_check != 0:
            all_fine = False
            break
        if digit_to_check == 0:
            all_fine = False
            break

    if all_fine:
        print(i_to_string, end=' ')



