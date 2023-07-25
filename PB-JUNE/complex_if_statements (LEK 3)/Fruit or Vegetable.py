product = input().lower()

fruit = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegetable = ['tomato', 'cucumber', 'pepper', 'carrot']
output = ''

if product in fruit:
    output = 'fruit'
elif product in vegetable:
    output = 'vegetable'
else:
    output = 'unknown'

print(output)