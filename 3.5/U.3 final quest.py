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

with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\test_task_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    test_task_link_data = list(reader)

with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\task.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    task_data = list(reader)

with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\task_attempt.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    task_attemp_data = list(reader)

for string in class_user_link_data:
    if string[2] == user_id and string[1] == class_id:
        id_temp = string[0]
        for user_tests in test_class_user_link_data:
            if user_tests[2] == id_temp:
                test_id = user_tests[1]
                class_user_link_id = user_tests[0]
                given_time = user_tests[3]  # 31.05.2025 10:00:00
                given_time_formated = datetime.datetime.strptime(given_time, "%d.%m.%Y %H:%M:%S")
                for attemp in test_attemp_data:
                    if class_user_link_id == attemp[1]:
                        test_attemp_id = attemp[0]
                        test_class_user_link_id = attemp[1]
                        break
                test_info_container.append([given_time_formated, test_attemp_id, test_id])
test_info_container.sort(reverse=True)
current_test = test_info_container.pop(0)
test_attemp_id = current_test[1]
test_id = current_test[2]

time_spended = 0
student_answers = {}
for task_attemp in task_attemp_data:
    if task_attemp[2] == test_attemp_id:
        student_answers[task_attemp[1]] = [task_attemp[3]]  # task_attemp[1] = id in task.csv
        if task_attemp[5] == '':
            pass
        else:
            time_spended += int(task_attemp[5])
hours = time_spended // 3600
minutes = (time_spended % 3600) // 60
seconds = time_spended % 60

true_answers = {}
for test_task_link in test_task_link_data:
    if test_task_link[1] == test_id:
        task_id = test_task_link[2]
        order_number = test_task_link[3]
        for task in task_data:
            if task[0] == task_id:
                true_answers[task[0]] = [task[2], order_number]
                break

last_test_info = []
tasks_count = len(true_answers)
answered_count = 0
true_answered_count = 0
for answer in true_answers:
    if answer not in student_answers or student_answers[answer][0] == '':
        last_test_info.append([f"{true_answers[answer][1]} ? {answer}"])
    elif student_answers[answer][0] == true_answers[answer][0]:
        last_test_info.append([f"{true_answers[answer][1]} TRUE {answer}"])
        answered_count += 1
        true_answered_count += 1
    else:
        last_test_info.append([f"{true_answers[answer][1]} FALSE {answer}"])
        answered_count += 1

print(f'{answered_count/tasks_count:.1%} {true_answered_count/answered_count:.1%}')
for info in last_test_info:
    print(''.join(info))
print(f"{hours:02}:{minutes:02}:{seconds:02}")
