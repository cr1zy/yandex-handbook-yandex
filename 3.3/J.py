words = 'Ехали медведи на велосипеде'
lst = [word for word in words.split() if sum(1 for letter in word if letter.lower() in 'аяуюоёэеиыaeiouy') >= 3]
print(lst)

# 30 mins