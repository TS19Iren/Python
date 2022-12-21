# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]
print(f'Первоначальный набор вещественных чисел: {my_list}')
new_list = []
for i in my_list:
    new_list.append(round(i - int(i), 2))
print(f'Значения дробной части массива: {new_list}')


def searching_max(my_list):
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    print(f'Максимальное значение : {max}')
    return max

def searching_min(my_list):
    min = my_list[0]
    for i in my_list:
        if 0 < i < min:
            min = i
    print(f'Минимальное значение: {min}')
    return min

result = searching_max(new_list)-searching_min(new_list)
print(f'Разница между максимальным и минимальным значением дробной части: {result}')

