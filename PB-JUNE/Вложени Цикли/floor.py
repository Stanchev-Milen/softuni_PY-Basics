floors = int(input())
rooms = int(input())

for f in range(floors, 0, -1):
    for r in range(rooms):
        if floors == 1 or f == floors:
            print(f'L{f}{r} ', end='')
        elif floors != 1 and f != floors:
            if f % 2 == 0:
                print(f'O{f}{r} ', end='')
            elif f % 2 != 0:
                print(f'А{f}{r} ', end='')
    print()
