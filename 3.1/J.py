letters = []
while (text := input().lower()) != 'финиш':
    for letter in text:
        letters.append(letter)
print(letters)
