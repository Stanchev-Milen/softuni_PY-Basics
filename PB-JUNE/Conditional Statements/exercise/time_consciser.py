#Input

hours = int(input())
minutes = int(input())

# Logic NEW TIME
minutes += 15
hours += minutes // 60
minutes = minutes % 60

if hours >= 24:
    hours = 0
if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f"{hours}:{minutes}")
