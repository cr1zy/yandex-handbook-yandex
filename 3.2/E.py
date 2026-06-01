man_count = int(input())
ovs_count = int(input())
kids = set()

for i in range(man_count + ovs_count):
    if (kid := input()) not in kids:
        kids[kid] = 1
    else:
        kids[kid] += 1

    man.add(input())
for i in range(ovs_count):
    ovs.add(input())
if ovs ^ man == set():
    print('Таких нет')
else:
    s = 0
    for i in ovs ^ man:
        s += 1
    print(s)


# 2 min

# создаём пустой словарь
countries = dict()
# вводим первую строку до цикла (можно заменить, использовав оператор-морж)
country = input()
# создаём счётчик номеров строк
str_number = 0
# продолжаем цикл, пока не введена строка «СТОП»
while country != "СТОП":
    # если введённой страны нет в словаре, создаём ключ и записываем по ключу список из одного номера строки
    if country not in countries:
        countries[country] = [str_number]
    # иначе добавляем в список по ключу новое значение номера строки
    else:
        countries[country].append(str_number)
    # увеличиваем счётчик
    str_number += 1
    # вводим следующую строку
    country = input()
# выводим название страны и полученные списки с новой строки
for country in countries:
    print(f"{country}: {countries[country]}")
