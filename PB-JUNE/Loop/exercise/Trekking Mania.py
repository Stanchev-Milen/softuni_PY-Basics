#Input
groups_qty = int(input())

#logic
total_members_musala = 0
total_members_monblan = 0
total_members_kilimandjaro = 0
total_members_k2 = 0
total_members_everest = 0

for i in range(groups_qty):
    size_of_group = int(input())
    if size_of_group <= 5:
        total_members_musala += size_of_group
    elif 6 <= size_of_group <= 12:
        total_members_monblan += size_of_group
    elif 13 <= size_of_group <= 25:
        total_members_kilimandjaro += size_of_group
    elif 26 <= size_of_group <= 40:
        total_members_k2 += size_of_group
    elif size_of_group >= 41:
        total_members_everest += size_of_group

all_members = total_members_musala + total_members_monblan + total_members_kilimandjaro + total_members_k2 + total_members_everest

percent_musala = 100 * (total_members_musala / all_members)
percent_monblan = 100 * (total_members_monblan / all_members)
percent_kilimandjaro = 100 * (total_members_kilimandjaro / all_members)
percent_k2 = 100 * (total_members_k2 / all_members)
percent_everest = 100 * (total_members_everest / all_members)

#output
print(f'{percent_musala:.2f}%')
print(f'{percent_monblan:.2f}%')
print(f'{percent_kilimandjaro:.2f}%')
print(f'{percent_k2:.2f}%')
print(f'{percent_everest:.2f}%')