square_meters = float(input())

price_square_meter = float (square_meters * 7.61)
discount = 18/100 * price_square_meter

end_price = (price_square_meter - (18/100 * price_square_meter))

print(f'The final price is: {end_price} lv.')
print(f'The discount is: {discount} lv.')

