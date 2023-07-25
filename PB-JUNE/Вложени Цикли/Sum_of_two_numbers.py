#In
num1 = int(input())
num2 = int(input())
magic_num = int(input())

#Lo
flag = False
counter = 0

while True:
    for i in range(num1, num2 + 1):
        for j in range(num1, num2 + 1):
            sum = i + j
            if sum != magic_num:
                counter += 1
            elif sum == magic_num:
                counter += 1
                print(f'Combination N:{counter} ({i} + {j} = {magic_num})')
                flag = True
            if flag:
                break
        if flag:
            break
    if flag:
        break
    if not flag:
        print(f'{counter} combinations - neither equals {magic_num}')
        break




#Out