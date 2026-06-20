def key(x):
    value = x[1]
    if not isinstance(value, list):
        return False
    for number in x[1]:
        if number % 2 == 0:
            return True
    return False



# print(dict(filter(
#     key,
#     {'first': 2, 'second': '2 + 2 = 4', 'third': [1, 2, 3]}.items()
# )))

lambda x: isinstance(x[1], list) and any(isinstance(number, int) and number % 2 == 0 for number in x[1])
lambda v: isinstance(v[1], list) and any(isinstance(x, int) and x % 2 == 0 for x in v[1])
