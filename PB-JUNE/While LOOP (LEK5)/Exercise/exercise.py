my_string = 'abrakadabr!a'

for i in range(1, len(my_string,)):
    char = my_string[i]
    if char != '!':
        print(f'not i')
    else:
        print(i)
        print('HOORAY')
    if char == '!':
        break