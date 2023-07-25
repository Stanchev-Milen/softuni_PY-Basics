# Input
record = float(input())
distance = float(input())
time_for_a_meter = float(input())

# Logic
delays = (distance // 15) * (12.5)
total_time = (time_for_a_meter * distance) + delays
seconds_needed = abs(record - total_time)

if total_time < record:
    print(f"Yes, he succeeded! The new world record is{total_time: .2f} seconds.")
else:
    print(f"No, he failed! He was{seconds_needed: .2f} seconds slower.")




# Output