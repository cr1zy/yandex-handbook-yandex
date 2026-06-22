def make_equation(*args):
    if len(args) == 1:
        return f"{args[0]}"
    return f"({make_equation(*args[:-1])}) * x + {args[-1]}"

print(make_equation(1, 2 ,3, 4, 5))


