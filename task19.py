# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


# Функция генерации сл. чисел от 0 до 100
def rnd():
    return random.randint(0, 101)


# генерация множителей многочлена
# ratio - коэф многочлена
def generate_polinomial_values(ratio):
    pol = []
    for i in range(ratio + 1):
        pol.append(rnd())

    return pol


# генерация многочлена в виде строки
def generate_polinomial_string(pol_vals):
    pol_str = ''
    for index in range(len(pol_vals) - 1, -1, -1):
        if pol_vals[index] != 0:
            if index == 1:
                pol_str += f'{pol_vals[index]}*x'
            else:
                if index == 0:
                    pol_str += f'{pol_vals[index]}'
                else:
                    if pol_vals[index] == 1:
                        pol_str += f'x^{index}'
                    else:
                        pol_str += f'{pol_vals[index]}*x^{index}'
            if index != 0:
                pol_str += ' + '
    pol_str += ' = 0'
    if pol_str.startswith(' + '):
        pol_str = pol_str.replace(' + ', '', 1)
    pol_str = pol_str.replace(' + 0 = ', ' = ')
    pol_str = pol_str.replace(' +  = 0', ' = 0')
    return pol_str


def write_file(pol_string):
    with open('task19_output.txt', 'w') as data:
        data.write(pol_string)


ratio = int(input("Введите натуральную степень k = "))
pol_vals = generate_polinomial_values(ratio)
pol_string = generate_polinomial_string(pol_vals)
print(f'Сгенерированный многочислен {pol_string}')
print('Записываем в файл...')
write_file(pol_string)
print('Данные записаны в файл')
