# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]
# my_list = [2, 3, 5, 6]
new_list = []
element = 0
lenOfList = 0
if len(my_list) % 2 == 0:
    lenOfList = int(len(my_list) / 2)
else:
    lenOfList = int(len(my_list) / 2) + 1
for index in range(lenOfList):
    new_list.append(my_list[index] * my_list[len(my_list) - 1 - index])
print(new_list)
