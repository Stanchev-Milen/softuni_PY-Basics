interval_start = int(input())
interval_end = int(input())
is_special = False

for i in range(interval_start, interval_end + 1):
    for j in range(interval_start, interval_end + 1):
        for k in range(interval_start, interval_end + 1):
            for l in range(interval_start, interval_end + 1):
                sum_second_third_digit = j + k

                if i % 2 == 0 and l % 2 != 0:
                    is_special = True
  ь              elif i % 2 != 0 and l % 2 == 0:
                    is_special = True
                if not i > l:
                    is_special = False
                if sum_second_third_digit % 2 != 0:
                    is_special = False

                if is_special:
                sum_second_third_digit = 0
                    print(f'{i}{j}{k}{l}', end=' ')
                is_special = False
