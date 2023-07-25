#In

tournament_qty = int(input())
starting_points = int(input())

#Lo
from math import floor

total_points = starting_points
count_wins = 0
count_finals = 0
count_semifinal = 0

for i in range(tournament_qty):
    tournament_achievement = input()
    if tournament_achievement == 'W':
        total_points += 2000
        count_wins += 1
    elif tournament_achievement == 'F':
        total_points += 1200
        count_finals += 1
    elif tournament_achievement == 'SF':
        total_points += 720
        count_semifinal += 1

won_points = total_points - starting_points
average_gained_points_per_tournament = floor(won_points / tournament_qty)
percent_wins = (count_wins / (count_semifinal + count_finals + count_wins)) * 100


#Out
print(f'Final points: {total_points}')
print(f'Average points: {average_gained_points_per_tournament}')
print(f'{percent_wins:.2f}%')