# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
number = input('Введите число: ')
sum = 0
for c in number:

    if c != ',' and c != '.':
        sum = sum + float(c)
print(int(sum))
