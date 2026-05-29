N, M, Q, cw, sw, hw, tw = map(int, input().split()) 
if M > 0 and N >= 3 and min(cw, sw, hw, tw) > 0 and Q > 0:
    Flag = False
    top1_rating = 0
    top2_rating = 0
    top3_rating = 0
    pre_average_rating = 0
    min_rating = 100
    top1_rating_name = ''
    top2_rating_name = ''
    top3_rating_name = ''
    for student in range(N):
        name = input()
        a = b = c = d = 0
        for lessons in range(M):
            ai, bi, ci, di = map(int, input().split(","))
            a = a + ai * cw
            b = b + bi * sw
            c = c + ci * hw
            d = d + di * tw
        rating = (((a + b + c + d) / Q) * 100)
        if rating > 100:
            Flag = True
        min_rating = min(min_rating, rating)
        if top1_rating < rating:
            top3_rating, top2_rating, top1_rating = top2_rating, top1_rating, rating
            top3_rating_name, top2_rating_name, top1_rating_name = top2_rating_name, top1_rating_name, name
        elif top2_rating < rating:
            top3_rating, top2_rating = top2_rating, rating
            top3_rating_name, top2_rating_name = top2_rating_name, name
        elif top3_rating < rating < top2_rating:
            top3_rating = rating
            top3_rating_name = name
        pre_average_rating += rating
    average_rating = round(pre_average_rating / N)
    if average_rating < 50:
        average_rating_message = 'Курс усваивается плохо'
    else:
        average_rating_message = 'Курс усваивается хорошо'
    if Flag:
        print("Во введённых данных ошибка")
    else:
        print(
            f"{round(top1_rating)} {average_rating} {round(min_rating)}\n"
            f"{top1_rating_name} {round(top1_rating)}%\n"
            f"{top2_rating_name} {round(top2_rating)}%\n"
            f"{top3_rating_name} {round(top3_rating)}%\n"
            f"{average_rating_message}"
        )
else:
    print("Во введённых данных ошибка")