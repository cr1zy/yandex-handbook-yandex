result = -1
h_recent = 0

for i in range(int(input())):
    b = int(input())
    m = b // 256 ** 2
    r = (b - m * 256 ** 2) // 256
    h = b - r * 256 - m * 256 ** 2
    if h >= 100 or h != (37 * (m + r + h_recent)) % 256:
        result = i
        break
    h_recent = h

print(result)
