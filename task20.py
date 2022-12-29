# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.

#Чтение из памяти в строку
def read_file(filename):
    with open(filename, 'r') as data:
        list = data.readlines()
        str = ''
        for i in list:
            str += i
        return str

#сложение многочленов
def polinominal_summary(pol_str1, pol_str2):
    pol_val1 = parse_pol_str(pol_str1)
    pol_val2 = parse_pol_str(pol_str2)
    short_pol_vals = pol_val1
    long_pol_vals = pol_val2
    if len(pol_val2) < len(pol_val1):
        short_pol_vals = pol_val2
        long_pol_vals = pol_val1

    res_pol_vals = []
    for i in range(len(long_pol_vals) - 1, len(short_pol_vals) - 1, -1):
        res_pol_vals.append(int(long_pol_vals[i]))

    for i in range(len(short_pol_vals) - 1, -1, -1):
        res_pol_vals.append(int(short_pol_vals[i]) + int(long_pol_vals[i]))

    return res_pol_vals


#преобразование строки многочлена в массив, где индекс - стпень многочлена, значение - множитель
def parse_pol_str(pol_str):
    pol_val_with_index_as_ratio = []
    #убираем все лишние символы
    pol_str = pol_str.replace(' ', '').replace('*', '').replace('^', '').replace('=0', '')
    #разбиваем на список множителей и многочленов
    pol_vals = pol_str.split('+')

    for index, item in enumerate(pol_vals):
        #разбиваем многочлена на множитель и степень
        step_val = item.split('x')
        # т.к. на первом шаге у нас наибольшая степень - инициируем нулями
        if index == 0:
            for i in range(int(step_val[1]) + 1):
                pol_val_with_index_as_ratio.append('0')
        if len(step_val) == 2:
            if step_val[1] == '':
                step_val[1] = '1'
            if step_val[0] == '':
                step_val[0] = '1'
            pol_val_with_index_as_ratio[int(step_val[1])] = step_val[0]
        else:
            if len(step_val) == 1:
                pol_val_with_index_as_ratio[0] = step_val[0]

    return pol_val_with_index_as_ratio


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
    with open('task20_output.txt', 'w') as data:
        data.write(pol_string)

pol_str1 = read_file("task20_input1.txt")
pol_str2 = read_file("task20_input2.txt")


print(f'Данные из первого файла: {pol_str1}')
print(f'Данные из второго файла: {pol_str2}')
pol_val_sums = polinominal_summary(pol_str1, pol_str2)
result_pol_str = generate_polinomial_string(pol_val_sums[::-1])
print(result_pol_str)
write_file(result_pol_str)

