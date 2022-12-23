# Найдите корни квадратного уравнения Ax² + Bx + C = 0 с помощью математических формул нахождения корней квадратного уравнения
import math

data = "3 * x  2 - 14 * x - 5 = 0"
# data = "1 * x  2 + 6 * x + 9 = 0"

data_list = data.split()
var_list = []

for i in range(len(data_list)):
    if data_list[i].isdigit():
        if i > 0 and data_list[i-1] == '-':
            var_list.append(-1 * int(data_list[i]))
        else:
            var_list.append(int(data_list[i]))

print(var_list)

a, b, c = var_list[0], var_list[2], var_list[3]

disc = var_list[2] ** 2 - (4 * var_list[0] * var_list[3])

print(disc)

if disc > 0:
    x1 = (-var_list[2] + math.sqrt(disc)) / (2 * var_list[0])
    x2 =  (-var_list[2] - math.sqrt(disc)) / (2 * var_list[0])
    print(f'x1: {round(x1, 2)}, x2: {round(x2, 2)}')
elif disc == 0:
    x = (-var_list[2]) / (2 * var_list[0])
    print(f'x: {x}')
else:
    x = None
    print('Действительных корней нет')