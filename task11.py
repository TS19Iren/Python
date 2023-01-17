# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

text = ['abc', 'qwe','abe', 'we']
b = 'we'
# for item in text:
#     if item.find(str(b)) !=-1:
#         print(f'В строке {item} есть подстрока {b}')

# for item in range(len(text)):
#     if search = text[i]:
#         print(f'Подстрока встречается в искомом списке на индексе {i}')

# search = lambda x, y: True if y.find(x) != -1 else False
print(list(filter(lambda x: True if x.find(b) != -1 else False, text)))
