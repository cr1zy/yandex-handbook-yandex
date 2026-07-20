import math

x = float(input())

a = math.log(math.pow(x, 3 / 16), 32) 
b = math.pow(x, math.cos((math.pi * x) / (math.e * 2))) 
c = (math.sin(x / math.pi) ** 2)

print(a + b - c)
