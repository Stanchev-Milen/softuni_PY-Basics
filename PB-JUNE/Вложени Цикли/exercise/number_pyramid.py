num = int(input())
current = 1
all_true = False

for row in range(1, num + 1):
    for column in range(1, row + 1):
        print(current, end=' ')
        current += 1

        if current > num:
            all_true = True
            break

    if all_true:
        break

    print()




