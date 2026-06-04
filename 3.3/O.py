text = 'Мама мыла раму!'
# result = {}
# for index in set(text.lower()):
#     if index.isalpha():
#         result[index] = text.lower().count(index)
# print(result)

# for index in set(text.lower()):
#     if index.isalpha():
#         result[index] = text.lower().count(index)

x = {index: text.lower().count(index) for index in set(text.lower()) if index.isalpha()}
print(x)