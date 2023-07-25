#Input
fruit = input().lower()
weekday = input().lower()
qty = float(input())

#Logic
working_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
weekend_days = ['saturday', 'sunday']
price = 0
total_price = 0
is_input_correct = True

if weekday in working_days:
    if fruit == 'banana':
        price = 2.5
    elif fruit == 'apple':
        price = 1.20
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.70
    elif fruit == 'pineapple':
        price = 5.5
    elif fruit == 'grapes':
        price = 3.85
    else:
        is_input_correct = False

elif weekday in weekend_days:
    if fruit == 'banana':
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.90
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'kiwi':
        price = 3.00
    elif fruit == 'pineapple':
        price = 5.60
    elif fruit == 'grapes':
        price = 4.20
    else:
        is_input_correct = False

#Output
if is_input_correct == False:
    print('error')
elif weekday not in (working_days or weekend_days):
    print('error')
else:
    total_price = f'{price * qty:.2f}'
    print(total_price)

