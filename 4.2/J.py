def choice (*args,**kwargs):
    if "min" in kwargs:
        func = kwargs["min"]
        minmax = min
    else:
        func = kwargs["max"]
        minmax = max
    return minmax(map(func, args))
print(choice(1, 2, 3, 4, 5, max=lambda x: 2 ** x))