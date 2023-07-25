from time import sleep

for hours in range(0, 23 + 1):
    for minutes in range(0, 60):
        for seconds in range(0, 60):
            if minutes <= 9 and seconds <= 9:
                print(f'{hours}:0{minutes}:0{seconds}')
            else:
                print(f'{hours}:{minutes}:{seconds}')
            sleep(1)
#blblbllblb
print('Vanka')