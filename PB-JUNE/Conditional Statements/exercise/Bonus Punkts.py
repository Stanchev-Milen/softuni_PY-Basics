# Input
points_base = int(input())

# Logic
bonus_points = 0


if points_base <= 100:
    bonus_points = 5
elif points_base <= 1000:
    bonus_points = 0.2 * points_base
elif points_base > 1000:
    bonus_points = 0.1 * points_base
if points_base % 2 == 0:
    bonus_points += 1
elif points_base % 10 == 5:
    bonus_points += 2
total_points = points_base + bonus_points

# Output
print(bonus_points)
print(total_points)