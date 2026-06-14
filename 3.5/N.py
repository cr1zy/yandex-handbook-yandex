import json
from pathlib import Path

file_name_users = input()
file_name_updates = input()
# для работы на компьютере
# file_name_users = Path(r"D:\code\yandex-handbook-python\txts\3.5") / file_name_users
# file_name_updates = Path(r"D:\code\yandex-handbook-python\txts\3.5") / file_name_updates

with open(file_name_users, encoding="UTF-8") as file_in:
    records_users = json.load(file_in)

with open(file_name_updates, encoding="UTF-8") as file_in:
    records_updates = json.load(file_in)

for record_update in records_updates:
    for record_user in records_users:
        if record_user['name'] == record_update['name']:
            for key in record_update.keys():
                if record_update[key] > record_user.get(key, ''):
                    record_user[key] = record_update[key]

updated_records = {}

for record in records_users:
    name = record.pop('name')
    updated_records[name] = record

with open(file_name_users, 'w', encoding="UTF-8") as file_out:
    json.dump(updated_records, file_out, ensure_ascii=False, indent=4)