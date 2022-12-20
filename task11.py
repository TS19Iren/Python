# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

text = ['dkfhka', 'cjkjdfh','jsklf', 'dsdfjdf']
b = 'df'
for item in text:
    if item.find(str(b)) !=-1:
        print(f'В строке {item} есть подстрока {b}')

# for item in range(len(text)):
#     if search = text[i]:
#         print(f'Подстрока встречается в искомом списке на индексе {i}')