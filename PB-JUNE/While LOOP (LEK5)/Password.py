#in
username = input()
password = input()

#lo
while True:
    login_try = input()
    if login_try != password:
        print('Try again!')
    elif login_try == password:
        print(f'Welcome {username}!')
        break
