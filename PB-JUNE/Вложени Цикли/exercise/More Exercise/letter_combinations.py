interval_start = input()
interval_end = input()
letter_to_miss = input()

interval_start_to_ord = ord(interval_start)
interval_end_to_ord = ord(interval_end)
letter_to_miss_ord = ord(letter_to_miss)
combinations = 0

for letter in range(interval_start_to_ord, interval_end_to_ord + 1):
    if letter == letter_to_miss_ord:
        continue
    for letter_2 in range(interval_start_to_ord, interval_end_to_ord + 1):
        if letter_2 == letter_to_miss_ord:
            continue
        for letter_3 in range(interval_start_to_ord, interval_end_to_ord + 1):
            if letter_3 == letter_to_miss_ord:
                continue
            print(f'{chr(letter)}{chr(letter_2)}{chr(letter_3)}', end=' ')
            combinations += 1

print(combinations)
