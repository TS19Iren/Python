# Напишите программу, которая будет на вход принимать число N и выводить
# числа от - N до N
# *Примеры: *
# при
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
number = int(input('Введите число: '))

# for i in range(-number,number+1,1):
#     print(i, end=' ')

# my_list = []
# for i in range (-number,number+1):
#     my_list.append(i)
# print(*my_list, sep=', ')

my_list = []
for i in range (-number,number+abs(number)//number , abs(number)//number):
    my_list.append(i)
print(*my_list, sep=', ')

