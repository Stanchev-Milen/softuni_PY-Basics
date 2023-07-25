



NE RABOTI !!!!!!!!!!!!!!!!!


a = int(input())
b = int(input())
max_generated_passwords = int(input())

counter = 0
for A in range(35, 56):
    if counter == max_generated_passwords:
        break

    for B in range(64, 97):
        if counter == max_generated_passwords:
            break

        for x in range(1, a + 1):
            if counter == max_generated_passwords:
                break

            for y in range(1, b + 1):
                if counter == max_generated_passwords:
                    break

                password = chr(A) + chr(B) + str(x) + str(y) + chr(B) + chr(A)
                print(password, end='|')
                counter += 1

print()