les = dict()
while len(zveri := input().split()) != 0:
    for zver in zveri:
        if zver not in les:
            les[zver] = 1
        else:
            les[zver] += 1
for okr in les:
    print(f"{okr} {les[okr]}")

# 10 mins