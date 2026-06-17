import csv
import datetime

user_id, class_id = input().split()
test_info_container = []

with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\class_user_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    class_user_link_data = list(reader)

with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\test_class_user_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    test_class_user_link_data = list(reader)

with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\test_attempt.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    test_attemp_data = list(reader)

with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\test.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    test_data = list(reader)

for string in class_user_link_data:
    if string[2] == user_id and string[1] == class_id:
        id_temp = string[0]
        given_count = 0
        solved_count = 0
        for user_tests in test_class_user_link_data:
            if user_tests[2] == id_temp:
                test_id = user_tests[1]
                class_user_link_id = user_tests[0]
                given_count += 1
                given_time = user_tests[3]  # 31.05.2025 10:00:00
                given_time_formated = datetime.datetime.strptime(given_time, "%d.%m.%Y %H:%M:%S")
                test_status = 'FALSE'
                for test_info in test_data:
                    if test_info[0] == test_id:
                        title = test_info[1]
                for attemp in test_attemp_data:
                    if class_user_link_id == attemp[1] and attemp[2] == 'TRUE':
                        solved_count += 1
                        test_status = 'TRUE'
                        break
                test_info_container.append([given_time_formated, title, test_status])
test_info_container.sort(reverse=True)
print(f'{solved_count}/{given_count}')
for info in test_info_container:
    print(info[1], info[0].strftime("%d.%m.%y"), info[2])