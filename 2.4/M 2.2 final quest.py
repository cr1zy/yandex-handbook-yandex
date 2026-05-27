Flag = False
N, M, Q, cw, sw, hw, tw = map(int, input().split()) 
name = input()
if M == 0 or min(cw, sw, hw, tw) <= 0:
    Flag = True
else:
    a = b = c = d = 0
    for i in range(M):
        ai, bi, ci, di = map(int, input().split(","))
        a = a + ai * cw
        b = b + bi * sw
        c = c + ci * hw
        d = d + di * tw
    rating = round((((a + b + c + d)/Q)*100))
    if rating > 100:
        Flag = True
if Flag:
    print('Во введённых данных ошибка')
else:
    print(f'{name} {rating}%')
