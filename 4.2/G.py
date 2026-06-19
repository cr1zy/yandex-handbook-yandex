def get_formatter(end='',sep=' '):
    return lambda *numbers: sep.join(str(i) for i in numbers) + end
formatter = get_formatter()
print(formatter(1, 2, 3, 4, 5))