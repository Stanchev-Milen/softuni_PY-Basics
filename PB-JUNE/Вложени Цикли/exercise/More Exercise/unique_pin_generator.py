upper_limit_i = int(input())
upper_limit_j = int(input())
upper_limit_k = int(input())


for i in range(1, upper_limit_i + 1):
    if not i % 2 == 0:
        continue
    for j in range(2, upper_limit_j + 1):
        if not (j == 2 or j == 3 or j == 5 or j == 7):
            continue
        for k in range(1, upper_limit_k + 1):
            if not k % 2 == 0:
                continue
            print(f'{i} {j} {k}')
