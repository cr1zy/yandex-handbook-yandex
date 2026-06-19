def grow(*args, **kwargs):
    lst = []
    for arg in args:
        temp = 0 + arg
        for kwarg in kwargs:
            if arg % len(kwarg) == 0:
                temp += kwargs[kwarg]
        lst.append(temp)
    return lst
print(grow(1, 2, 3, 4, 5, ab=7, dad=10))
print(grow(12, 5, 30, 60, 15, first=13, second=2, Bob=7))