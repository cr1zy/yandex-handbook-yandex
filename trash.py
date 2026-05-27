# Создадим два списка с числами
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]

# Напишем функцию для сложения двух чисел
def add_numbers(x, y):
    return x + y

# Правильное использование map() с двумя списками ✅
result = list(map(add_numbers, numbers1, numbers2))
print(result)  # [11, 22, 33]