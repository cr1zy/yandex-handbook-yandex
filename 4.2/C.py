def gcd(*numbers):
    result = numbers[0]
    for x in numbers[1:]:
        while x:
            result, x = x, result % x
    return result