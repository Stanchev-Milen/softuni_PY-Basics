#0.40 за торбички

sq_meters_nylon = int(input())
liters_paint = int(input())
liters_thinner = int(input())
hours_work = int(input())

#Prices are in BGN10
price_nylon_per_sq_m = 1.5
price_paint_liter = 14.5
price_thinner_liter = 5

#f=final
f_price_nylon_per_sq_m = (price_nylon_per_sq_m * (2 + sq_meters_nylon))
f_price_paint_liter = (price_paint_liter * liters_paint) * 1.1
f_price_thinner_liter = (price_thinner_liter * liters_thinner)
total_sum = f_price_thinner_liter + f_price_paint_liter + f_price_nylon_per_sq_m + 0.40
work_expense =(hours_work * (0.3 * total_sum))

final_sum = total_sum + work_expense

print(round(final_sum, 2))
