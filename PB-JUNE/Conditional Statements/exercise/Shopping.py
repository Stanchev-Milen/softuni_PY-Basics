# Input  ; q - quantity
budget = float(input())
q_video_cards = int(input())
q_processors = int(input())
q_ram = int(input())

# Logic
video_cars_price = 250
processor_price = 0.35 * (q_video_cards * video_cars_price)
ram_price = 0.10 * (q_video_cards * video_cars_price)
total_price = (video_cars_price * q_video_cards) + (ram_price * q_ram) + (processor_price * q_processors)

if q_video_cards > q_processors:
    total_price *= 0.85

left_money = abs(budget - total_price)

if budget >= total_price:
    print(f'You have{left_money: .2f} leva left!')
else:
    print(f'Not enough money! You need{left_money: .2f} leva more!')

# Output