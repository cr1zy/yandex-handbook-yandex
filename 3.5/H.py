with open (r"D:\code\yandex-handbook-python\txts\3.5\H first.txt", encoding="UTF-8") as file_in:
    st1 = {word for word in file_in.read().split()}
with open (r"D:\code\yandex-handbook-python\txts\3.5\H second.txt", encoding="UTF-8") as file_in:
    st2 = {word for word in file_in.read().split()}
sus = st1 ^ st2
string = '\n'.join(sus)
with open(r"D:\code\yandex-handbook-python\txts\3.5\H answer.txt", "w", encoding="UTF-8") as file_out:
    file_out.write(
        string
    )