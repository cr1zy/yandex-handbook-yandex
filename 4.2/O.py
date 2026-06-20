def get_repeater(key, count):
    def repeater(value):
        x = value
        for _ in range(count):
            x = key(x)
        return x
    return repeater
repeater = get_repeater(lambda x: x + 1, 5)
print(repeater(2))

