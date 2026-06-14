with open (r"D:\code\yandex-handbook-python\txts\3.5\G numbers.txt", encoding="UTF-8") as file_in:
    lst = [int(number) for line in file_in for number in line.split()]
with open (r"D:\code\yandex-handbook-python\txts\3.5\G stats.txt", "w", encoding="UTF-8") as file_out:
    file_out.write(
        f"количество всех чисел: {len(lst)}\n"
        f"количество положительных чисел: {len([i for i in lst if i > 0])}\n"
        f"минимальное число: {min(lst)}\n"
        f"максимальное число: {max(lst)}\n"
        f"сумма всех чисел: {sum(lst)}\n"
        f"среднее арифметическое всех чисел с точностью до двух знаков после запятой: {sum(lst)/len(lst):.2f}\n"
    )