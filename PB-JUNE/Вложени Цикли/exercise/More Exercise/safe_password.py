a = int(input())
b = int(input())
max_generated_passwords = int(input())
count_combinations = 0
symbol_a = 35
symbol_b = 64
max_reached = False

for x in range(1, a + 1):
    for y in range(1, b + 1):
        combination = f'{chr(symbol_a)}{chr(symbol_b)}{x}{y}{chr(symbol_b)}{chr(symbol_a)}'
        count_combinations += 1

        if count_combinations > max_generated_passwords:
            max_reached = True
            break

        print(combination, end='|')
        symbol_b += 1
        symbol_a += 1

        if symbol_a > 55:
            symbol_a = 35
        if symbol_b > 96:
            symbol_b = 64
    if max_reached:
        break
