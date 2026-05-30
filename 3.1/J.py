letters = []
while (text := input()) != 'ФИНИШ':
    for letter in text.lower():
        letters.append(letter)
max_count = 0
max_letter = ''
for letter in letters:
    count = letters.count(letter)
    if count > max_count:
        max_count = count
        max_letter = letter
    elif count == max_count and letter < max_letter:
        max_letter = letter
print(max_letter)