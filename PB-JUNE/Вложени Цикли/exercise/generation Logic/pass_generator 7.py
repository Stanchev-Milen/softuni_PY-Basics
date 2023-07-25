a = int(input())
b = int(input())
number_of_passwords = int(input())
symbol_a = 35
symbol_b = 64
counter = 0
checking = True

for x in range(1, a + 1):
    if checking == False:
        break
    for y in range(1, b + 1):
        if counter == number_of_passwords:
            checking = False
            break
        print(f"{chr(symbol_a)}{chr(symbol_b)}{x}{y}{chr(symbol_b)}{chr(symbol_a)}|", end="")
        counter += 1
        symbol_a += 1
        symbol_b += 1
        if symbol_a > 55:
            symbol_a = 35
        if symbol_b > 96:
            symbol_b = 64