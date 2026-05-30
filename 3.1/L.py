menu = ['Манная','Гречневая','Пшённая','Овсяная','Рисовая']
days = int(input())
full_week = days // 5
part_week = days % 5
for _ in range(full_week):
    for delicios in menu:
        print(delicios)
for delicios in menu[:part_week]:
    print(delicios)