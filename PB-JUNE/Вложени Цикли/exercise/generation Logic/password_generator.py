secret = input()
counter = 0
is_found = False

for i in range(65, 122 +1):
    if i == 91 or i == 92 or i == 93 or i == 94 or i == 95 or i == 96:
        continue
    for j in range(65, 122 + 1):
        if j == 91 or j == 92 or j == 93 or j == 94 or j == 95 or j == 96:
            continue
        for k in range(65, 122 + 1):
            if k == 91 or k == 92 or k == 93 or k == 94 or k == 95 or k == 96:
                continue
            for l in range(65, 122 + 1):
                if l == 91 or l == 92 or l == 93 or l == 94 or l == 95 or l == 96:
                    continue
#                for m in range(65, 122 + 1):
 #                   if m == 91 or m == 92 or m == 93 or m == 94 or m == 95 or m == 96:
  #                      continue
                counter += 1
                combination = f'{chr(i)}{chr(j)}{chr(k)}{chr(l)}' #{chr(m)}
                if combination == secret:
                    print(counter)
                    print((combination))
                    is_found = True

                if is_found:
                    break
            if is_found:
                break
        if is_found:
            break
    if is_found:
        break
#    if is_found:
 #       break