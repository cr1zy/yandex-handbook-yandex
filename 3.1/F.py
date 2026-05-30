repeat = int(input())
count = 0
for i in range(repeat):
    some_string = input()
    count += some_string.count("зайка")
print(count)