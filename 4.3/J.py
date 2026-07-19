def make_linear(lst):
    linear_lst = []
    for i in lst:
        if not isinstance(i, list):
            linear_lst.append(i)
        else:
            linear_lst.extend(make_linear(i))
    return linear_lst

print(make_linear([1, [2, [3, 4]], 5, 6]))