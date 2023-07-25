movie_name = input()
total_for_all_movies = 0
all_student_tickets = 0
all_kid_tickets = 0
all_standard_tickets = 0

while movie_name != 'Finish':
    available_seats = int(input())
    total_tickets_sold = 0
    counter_student = 0
    counter_standard = 0
    counter_kid = 0

    for seat in range(available_seats):
        seat_type = input()

        if seat_type == 'End':
            break
        elif seat_type == 'student':
            counter_student += 1
        elif seat_type == 'standard':
            counter_standard += 1
        elif seat_type == 'kid':
            counter_kid += 1

    total_tickets_sold = counter_standard + counter_kid + counter_student
    total_for_all_movies += total_tickets_sold

    p_full = (total_tickets_sold / available_seats) * 100
    all_student_tickets += counter_student
    all_standard_tickets += counter_standard
    all_kid_tickets += counter_kid

    print(f'{movie_name} - {p_full:.2f}% full.')

    movie_name = input()

p_student = 100 * (all_student_tickets / total_for_all_movies)
p_standard = 100 * (all_standard_tickets / total_for_all_movies)
p_kid = 100 * (all_kid_tickets / total_for_all_movies)

print(f'Total tickets: {total_for_all_movies}')
print(f"{p_student:.2f}% student tickets.")
print(f"{p_standard:.2f}% standard tickets.")
print(f"{p_kid:.2f}% kids tickets.")


