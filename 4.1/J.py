def split_numbers(text):
    split_text = text.split()
    return tuple([int(i) for i in split_text])
print(split_numbers("1 -2 3 -4 5"))

