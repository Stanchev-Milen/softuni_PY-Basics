#Input
num = int(input())
validity = ''

#Logic
if 100 <= num <= 200 or num == 0:
    validity = ''
else:
    validity = 'invalid'

#Output
print(validity)