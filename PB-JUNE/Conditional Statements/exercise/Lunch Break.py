# Input
series_name = input()
series_duration = int(input())
break_duration = int(input())


# Logic
from math import ceil

lunch_duration = (0.125 * break_duration)
rest_duration = (0.25 * break_duration)
left_time = ceil(abs(break_duration - (lunch_duration + rest_duration + series_duration)))

if break_duration >= (lunch_duration + rest_duration + series_duration):
    print(f"You have enough time to watch {series_name} and left with {left_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {left_time} more minutes.")

# Output