def get_operator(operator: str):
    if operator == '+':
        return lambda a, b: a + b
    if operator == '-':
        return lambda a, b: a - b
    if operator == '*':
        return lambda a, b: a * b
    if operator == '//':
        
        return lambda a, b: a // b
    if operator == '**':
        return lambda a, b: a ** b

    raise ValueError(f"Unsupported operator: {operator}")

operator_power = get_operator("**")
print(operator_power(2, 10))