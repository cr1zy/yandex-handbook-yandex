def recursive_digit_sum(number):
    if not number:
        return 0
    return recursive_digit_sum(number // 10) + (number % 10)

print(recursive_digit_sum(7321346))