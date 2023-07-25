packs_of_pen = int(input())
packs_of_markers = int(input())
liters_of_chemical_for_whiteboard =int(input())
discount = int(input()) / 100

price_pack_pen = 5.80
price_pack_markers = 7.202

price_liter_chemical = 1.20

total_sum = ((packs_of_markers * price_pack_markers) + (packs_of_pen * price_pack_pen) + (price_liter_chemical * liters_of_chemical_for_whiteboard))
final_sum = total_sum - (discount * total_sum)

print(round(final_sum, 1))
