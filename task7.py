# Напишите программу, которая будет принимать
# на вход дробь и показывать первую цифру
# дробной части числа.
# *Примеры: *
# - 6, 78 -> 7
# - 5 -> нет
# - 0, 34 -> 3

number = float(input('Введите дробное число: '))
# result = int((number*10%10)
# print(result)

if(int(number)==number):
    print('no')
else:
    print(int(abs(number)*10)%10)