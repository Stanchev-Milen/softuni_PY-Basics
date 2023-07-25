from time import sleep

while True:
    for i in range(10, -1, -1):
        if i == 10:
            print('RED!!! 10 seconds until start :)')
        elif i != 10:
            print(i)
        sleep(1)
        if i == 0:
            break
    for i in range(3, -1, -1):
        if i == 3:
            print('Yellow!')
        elif i != 3:
            print(i)
        sleep(1)
        if i == 0:
            break
    for i in range(10, 0, -1):
        if i == 10:
            print('GREEN!!! GO!')
        elif i != 10:
            print(i)
        sleep(1)
        if i == 0:
            break