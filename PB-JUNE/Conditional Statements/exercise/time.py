# Input
hours = int(input())
minutes = int(input())

# Logic
minutes_new = minutes + 15
hours_new = hours + (minutes_new // 60)
minutes_new = minutes_new % 60

if hours_new >= 24:
    hours_new = 0
if minutes_new < 10:
    print(f'{hours_new}:0{minutes_new}')
else:
    print(f"{hours_new}:{minutes_new}")

# Output
