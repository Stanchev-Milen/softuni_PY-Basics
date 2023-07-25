#Input
time = int(input())
weekday = input().lower()

#Logic
working_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
open_close = ''

if weekday in working_days:
    if 10 <= time <= 18:
        open_close = 'open'
    else:
        open_close = 'closed'
else:
    open_close = 'closed'

#Output
print(open_close)
