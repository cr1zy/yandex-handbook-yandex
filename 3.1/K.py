titles = []
for i in range(int(input())):
    titles.append(input())
search_request = input().lower()
for title in titles:
    if search_request in title.lower():
        print(title)