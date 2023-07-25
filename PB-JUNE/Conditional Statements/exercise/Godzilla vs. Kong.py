# Input
budget = float(input())
film_extra  = int(input())
price_costume = float(input())

# Logic
decor =  0.1 * budget

if film_extra > 150:
    price_costume *= 0.9

total_expense = decor + (price_costume * film_extra)
money_needed = abs(budget - total_expense)

if total_expense > budget:
    print('Not enough money!')
    print(f'Wingard needs{money_needed: .2f} leva more.')
else:
    print("Action!")
    print(f'Wingard starts filming with{money_needed: .2f} leva left.')


# Output