# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

user_number = int(input('Введите десятичное число: '))


def binary_number(number):
    res = ''
    if number < 0:
        print('Введите не отрицательное число!')
    else:
        while number != 0:
            if number % 2 == 0:
                res = '0' + res
            else:
                res = '1' + res
            number = int(number / 2)
    return res


print(binary_number(user_number))
