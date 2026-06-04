data = {'a': [100], 'b': [20, 5], 'c': [7, 15, 3]}

x = min((sum(numbers), word) for word, numbers in data.items())[1]

print(x)
# 30 min spisano ❌