import json
from sys import stdin

answers = []
answer_iterator = iter(answers)
for answer in stdin:
    answers.append(answer.rstrip("\n"))

with open(r"D:\code\yandex-handbook-python\txts\3.5\O scoring.json", encoding="UTF-8") as file_in:
    records = json.load(file_in)

score = 0

for dct_layer1 in records:
    ball = dct_layer1['points'] // len(dct_layer1['tests'])
    for dct_layer2 in dct_layer1['tests']:
        if dct_layer2['pattern'] == next(answer_iterator):
            score += ball

print(score)