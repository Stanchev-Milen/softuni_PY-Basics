#Input
word = input()

#logic
sum = 0
length_of_word = len(word)

for i in range(len(word)):
    letter = word[i]
    if letter == 'a':
        sum += 1
    elif letter == 'e':
        sum += 2
    elif letter == 'i':
        sum += 3
    elif letter == 'o':
        sum += 4
    elif letter == 'u':
        sum += 5
#output
print(sum)
