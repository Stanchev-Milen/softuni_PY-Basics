n = int(input())


for row in range(1, n + 1):
    for space in range(n - row):
        print(' ', end='')
    for el in range(row):
        print('*', end=' ')

    print()

    if row == n:
        break


for r_row in range(n - 1,  0, -1):
    for space in range(n - r_row):
        print(' ', end='')
    for el in range(r_row):
        print('*', end=' ')
    if r_row == 1:
        break
    print()





