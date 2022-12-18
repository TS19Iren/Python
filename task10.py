# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int
import random

arrLen = int(input('Укажите длину массива: '))


def create_random_list(arrLen):
    my_list = []
    for i in range(arrLen):
        my_list.append(random.randint(1, 20))
    return my_list


rndList = create_random_list(arrLen)
print('Сгенерированный массив случайных чисел: ', rndList)


def replace_random_list(list):
    for index, item in enumerate(list):
        rndPosition = random.randint(0, len(list) - 1)
        valueAtRndPos = list[rndPosition]
        list[rndPosition] = list[index]
        list[index] = valueAtRndPos


replace_random_list(rndList)

print('Массив после перестановки случайным образом: ', rndList)
