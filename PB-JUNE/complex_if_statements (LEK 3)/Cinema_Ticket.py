#Input
day = input().lower()

#Logic
price = 0

if day == 'monday' or day == 'tuesday' or day == 'friday':
    price = 12
elif day == 'wednesday' or day == 'thursday':
    price = 14
elif day == 'saturday' or 'sunday':
    price = 16

#Output
print(price)