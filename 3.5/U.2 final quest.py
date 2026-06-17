import csv
import datetime

user_id, class_id = input().split()
test_info_container = []

with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\class_user_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    class_user_link_data = list(reader)
    for i in class_user_link_data:
        if i[2] == user_id and i[1] == class_id:
            id_temp = i[0]

with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\test_class_user_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    test_class_user_link_data = list(reader)
    given_count = 0
    solved_count = 0
    for i in test_class_user_link_data:
        if i[2] == id_temp:
            test_id = i[1]
            class_user_link_id = i[0]
            given_count += 1
            given_time = i[3] # 31.05.2025 10:00:00
            given_time_formated = datetime.datetime.strptime(given_time, "%d.%m.%Y %H:%M:%S")
            
            with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\test_attempt.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                test_attemp_data = list(reader)
                test_status = 'FALSE'
                for i in test_attemp_data:
                    if class_user_link_id == i[1]:
                        if i[2] == 'TRUE':
                            test_status = 'TRUE'
                        else:
                            test_status = 'FALSE'
                if test_status == 'TRUE':
                    solved_count += 1
            with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\test.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                test_data = list(reader)
                for i in test_data:
                    if i[0] == test_id:
                        title = i[1]
            test_info_container.append([title, given_time_formated.strftime("%d.%m.%y"), test_status])
print(f'{solved_count}/{given_count}')
for i in test_info_container:
    print(i[0], i[1], i[2])