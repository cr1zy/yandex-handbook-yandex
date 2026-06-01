str_numbers = input().lower().split()
a = "".join(str_numbers)
if a == a[::-1]:
    print("YES")
else:
    print("NO")