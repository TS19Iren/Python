# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc


def read_file(filename):
    with open(filename, 'r') as data:
        list = data.readlines()
        str = ''
        for i in list:
            str += i
        return str

def squeezing_string(string_to_squeeze):
    string_to_squeeze = list(string_to_squeeze)
    squeezed_string = ''
    count = 1
    i = 0
    while i <= len(string_to_squeeze) - 1:
        if i == len(string_to_squeeze) - 1:
            if string_to_squeeze[i] == string_to_squeeze[i - 1]:
                squeezed_string += str(count) + string_to_squeeze[i]
            else:
                squeezed_string+='1'+string_to_squeeze[i]
            break
        if string_to_squeeze[i] == string_to_squeeze[i + 1]:
            count = count + 1

        else:
            squeezed_string = squeezed_string + str(count) + string_to_squeeze[i]
            count = 1
        i = i + 1
    return squeezed_string
def unsqueezing_string(squeezed_string):
    squeezed_string = list(squeezed_string)
    unsqueezed_string = ''
    for i in range(0, len(squeezed_string)-1, 2):
        elem = int(squeezed_string[i]) * squeezed_string[i+1]
        unsqueezed_string += elem
    return unsqueezed_string

def write_file(string):
    with open('task26_output', 'w') as data:
        data.write(string)


string_to_squeeze = read_file('task26_input')

squeezed_string = squeezing_string(string_to_squeeze)
print(squeezed_string)
unsqueezed_string = unsqueezing_string(squeezed_string)
print(unsqueezed_string)
write_file(unsqueezed_string)



