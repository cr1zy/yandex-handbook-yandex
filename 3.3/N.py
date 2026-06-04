data = {'a': [1, 2, 3], 'b': [5, 2, 5], 'c': [7, 15, 3]}

# x = min((sum(numbers), word) for word, numbers in data.items())[1]

for word, numbers in data.items():
    for chislo in numbers:
        print(numbers.count(chislo))
        
x = {word for word, numbers in data.items() for chislo in numbers if numbers.count(chislo) > 1}
print(x)