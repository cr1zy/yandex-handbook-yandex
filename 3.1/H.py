repeat = int(input())
for i in range(repeat):
    some_string = input()
    index = some_string.find('зайка')
    if index != -1:
        print(index + 1)
    else:
        print('Заек нет =(')