# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [2, 3, 5, 9, 3, 4, 11, 14]
# summ = 0
# for i in range(1,len(my_list),2):
#     summ = my_list[i]+summ
# print(f'Сумма элементов на нечетных позициях {summ}')


res = [ele for idx, ele in enumerate(my_list) if idx % 2 != 0]
print(res)
