words = set()
for i in range(int(input())):
    words = words | set(input().split())
for i in words:
    print(i)

# 20 mins