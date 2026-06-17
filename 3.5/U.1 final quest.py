import csv

with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\user.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    user_csv_len = len(list(reader))
with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\class.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    class_csv_len = len(list(reader))
with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\class_user_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    class_user_link_csv_len = len(list(reader))
with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\task.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    task_csv_len = len(list(reader))
with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\test.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    test_csv_len = len(list(reader))
with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\test_task_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    test_task_link_csv_len = len(list(reader))
with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\test_class_user_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    test_class_user_link_csv_len = len(list(reader))
with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\test_attempt.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    test_attempt_csv_len = len(list(reader))
with open(r"D:\code\yandex-handbook-python\txts\3.5 final quest\task_attempt.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    task_attempt_csv_len = len(list(reader))

print(user_csv_len, class_csv_len, class_user_link_csv_len, 
      task_csv_len, test_csv_len, test_task_link_csv_len, 
      test_class_user_link_csv_len, test_attempt_csv_len, task_attempt_csv_len)
