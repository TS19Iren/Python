# Задайте список из n чисел последовательности (1 + 1/n)^n,
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06
from decimal import Decimal

number = int(input('Введите число: '))
# my_list = []
# new_number = 0
# summ = 0
# if number == 0:
#     print('Введите число больше 0!')
# else:
#     for n in range(1, number + 1):
#         new_number = round((1 + (1 / n)) ** n, 2)
#         my_list.append(new_number)
#         summ = summ + new_number
#     print(f'Для number = {number} -> {my_list}')
#     print(f'Сумма элементов равна: {summ}')

ariph = lambda x: round((1 + 1 / x) ** x, 2)
list_num = [ariph(i) for i in range(1, number + 1)]
print(list_num)
