def product(*args, **kwargs):
    for arg in args:
        arg = set(arg.lower())
    return arg
print(product("Ann", "Bob", A=2, n=7, b=3))