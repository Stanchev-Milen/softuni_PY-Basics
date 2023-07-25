#input
age = int(input())
p_laundry_machine = float(input())
p_toy_for_sale = int(input())

#logic
toy_qty = 0
profit_from_toys = 0
sum_cash = 0
cash = 0

for i in range(1, age +1):
    if i % 2 == 0:
        if i == 2:
            cash = 9
        if i != 2:
            cash += 10 * (i / 2) - 1
    elif i % 2 != 0:
        toy_qty += 1

profit_from_toys = toy_qty * p_toy_for_sale
sum_cash = cash + profit_from_toys
money_left = abs(sum_cash - p_laundry_machine)

#output
if sum_cash >= p_laundry_machine:
    print(f'Yes! {money_left:.2f}')
else:
    print(f'No! {money_left:.2f}')