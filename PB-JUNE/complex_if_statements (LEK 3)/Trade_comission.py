#Input
city = input()
trade_volume = float(input())


#logic
commission = 0
is_input_valid = True

if 0 <= trade_volume <= 500:
    if city == 'Sofia':
        commission = 0.05
    elif city == 'Varna':
        commission = 0.045
    elif city == 'Plovdiv':
        commission = 0.055
    else:
        is_input_valid = False

if 500 < trade_volume <= 1000:
    if city == 'Sofia':
        commission = 0.07
    elif city == 'Varna':
        commission = 0.075
    elif city == 'Plovdiv':
        commission = 0.08
    else:
        is_input_valid = False

if 1000 < trade_volume <= 10000:
    if city == 'Sofia':
        commission = 0.08
    elif city == 'Varna':
        commission = 0.1
    elif city == 'Plovdiv':
        commission = 0.12
    else:
        is_input_valid = False


if trade_volume > 10000:
    if city == 'Sofia':
        commission = 0.12
    elif city == 'Varna':
        commission = 0.13
    elif city == 'Plovdiv':
        commission = 0.145
    else:
        is_input_valid = False

total_commission = trade_volume * commission

#output
if trade_volume < 0:
    print('error')
elif is_input_valid == False:
    print('error')
else:
    print(f'{total_commission:.2f}')