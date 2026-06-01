stack = input().split()
result = []
for i in stack:
    if i.isdigit():
        result.append(int(i))
    else:
        c, b, a = result.pop(), result.pop(), result.pop()
        if i in "+-*":
            if i == "+":
                result.append(a + b)
            elif i == "-":
                result.append(a - b)
            elif i == "*":
                result.append(a * b)
        elif i in "~!#":
            if i == "~":
                result.append(a + b)
            elif i == "!":
                result.append(a - b)
            elif i == "#    ":
                result.append(a * b)
            pass
        elif i in "@":
            pass
print(result[0])

# 5 mins