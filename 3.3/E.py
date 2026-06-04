numbers = [number for number in range(16, 100, 4)]
setset = {x for x in numbers if x == int(x ** 0.5) ** 2}
print(setset)

# 15 mins