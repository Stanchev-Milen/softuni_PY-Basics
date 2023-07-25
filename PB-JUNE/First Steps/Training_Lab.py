w = float(input())
h = float(input())

# x = number of desks per w; y = per h; n = number of work places
y = int(w / 1.2)
x = int((h - 1) / 0.7)

n = int((x * y) - 3)

print(int(n))
