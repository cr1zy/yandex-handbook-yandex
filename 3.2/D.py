man_count = int(input())
man = set()
ovs_count = int(input())
ovs = set()

for i in range(man_count):
    man.add(input())
for i in range(ovs_count):
    ovs.add(input())
if ovs & man == set():
    print('Таких нет ')
else:
    s = 0
    for i in ovs & man:
        s += 1
    print(s)


# 25 min