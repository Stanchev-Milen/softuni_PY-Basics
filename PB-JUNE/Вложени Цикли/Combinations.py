num = int(input())
sum = 0
counter = 0

for i in range(num + 1):
    for j in range(num + 1):
        for k in range(num + 1):
            sum = i + j + k
            if sum == num:
                counter += 1
print(counter)



