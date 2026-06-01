stack = input().split()
result = []
for i in stack:
    if i.isdigit():
        result.append(int(i))
    else:
        if i in "+-*/":
            b, a = result.pop(), result.pop()
            if i == "+":
                result.append(a + b)
            elif i == "-":
                result.append(a - b)
            elif i == "*":
                result.append(a * b)
            elif i == '/':
                result.append(a // b)
        elif i in "~!#":
            a = result.pop()
            if i == "~":
                result.append(-a)
            elif i == "!":
                number = 1
                for _ in range(1, a + 1):
                    number *= _
                result.append(number)
            elif i == "#":
                result.extend([a, a])
        elif i in "@":
            c, b, a = result.pop(), result.pop(), result.pop()
            result.extend([c, b, a])
print(result[0])

# 10 mins