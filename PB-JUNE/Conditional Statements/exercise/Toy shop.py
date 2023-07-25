# Input;   Q- quantity
holiday_price = float(input())
q_puzzles = int(input())
q_speaking_dummies = int(input())
q_teddy_bears = int(input())
q_minions = int(input())
q_truck = int(input())

# Logic
puzzle_price = 2.60 * q_puzzles
speaking_dummy_price = 3 * q_speaking_dummies
teddy_bear_price = 4.1 * q_teddy_bears
minion_price = 8.2 * q_minions
truck_price = 2 * q_truck

profit = puzzle_price + truck_price + minion_price + speaking_dummy_price + teddy_bear_price
total_quantity = q_puzzles + q_truck + q_minions + q_teddy_bears + q_speaking_dummies

if total_quantity >= 50:
    profit *= 0.75

profit *= 0.9

needed_money = abs(profit - holiday_price)

if profit >= holiday_price:
    print(f'Yes!{needed_money: .2f} lv left.')
else:
    print(f"Not enough money!{needed_money: .2f} lv needed.")

# Output