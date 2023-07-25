number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menus = int(input())

#prices are in BGN
price_chicken_menu = 10.35
price_fish_menu = 12.40
price_vegetarian_menu = 8.15

total_sum = (number_of_fish_menus * price_fish_menu) + (number_of_vegetarian_menus * price_vegetarian_menu) + (number_of_chicken_menus * price_chicken_menu)
price_desert = total_sum * 0.20

final_sum = total_sum + price_desert + 2.50

print(round(final_sum, 2))