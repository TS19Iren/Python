# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
point_x = int(input('Введите координаты оси Х: '))
point_y = int(input('Введите координаты оси Y: '))
if point_x==0 or point_y==0:
    print('Введены неверные координаты, х и у не должны быть равны нулю')
else:
    if point_x>0:
        if point_y>0:
            print('Точка находится в 1 четверти')
        else:
            print('Точка находится в 4 четверти')
    else:
        if point_y > 0:
            print('Точка находится в 2 четверти')
        else:
            print('Точка находится в 3 четверти')