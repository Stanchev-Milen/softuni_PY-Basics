#Input

actor_name = input()
points_from_academy = float(input())
num_of_judges = int(input())

#logic
total_points = points_from_academy

for i in range(num_of_judges):
    judge_name = input()
    grade = float(input())
    total_points += (len(judge_name) * grade) / 2
    if total_points > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        break

points_needed = (1250.5 - total_points)
#output

if total_points <= 1250.5:
    print(f'Sorry, {actor_name} you need {points_needed:.1f} more!')
