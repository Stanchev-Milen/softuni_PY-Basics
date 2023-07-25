#Input
opem_tabs = int(input())
salary = float(input())

#Logic
for i in range(opem_tabs):
    name_tab = input()
    if name_tab == 'Facebook':
        salary -= 150
    elif name_tab == 'Instagram':
        salary -= 100
    elif name_tab == 'Reddit':
        salary -= 50
    if salary <= 0:
        break

#Output
if salary <= 0:
    print('You have lost your salary.')
else:
    print(int(salary))
