while (string := input()) != '':
    index = string.find('#')
    if index == 0:
        continue
    if index > 0:
        print(string[:index])
    else:
        print(string)