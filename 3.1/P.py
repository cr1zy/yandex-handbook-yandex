lenght = int(input())
Zagolovki = []
for i in range(int(input())):
    Zagolovki.append(input())
if len("".join(Zagolovki)) <= lenght:
    print("".join(Zagolovki))
else:
    lenght -= 3
    for Zagolovok in Zagolovki:
        if len(Zagolovok) < lenght:
            print(Zagolovok)
            lenght -= len(Zagolovok)
        else:
            print(Zagolovok[:lenght] + "...")
            break