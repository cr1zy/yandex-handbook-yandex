# rle = [('a', 2), ('b', 3), ('c', 1)]
rle = [('1', 1), ('0', 2), ('5', 1), ('0', 2)]
# for i in rle:
#     for b in range(i[1]):
#         print(i[0])

s = ''.join(i[0] for i in rle for b in range(i[1]))
print(s)