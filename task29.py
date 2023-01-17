# 1.# Напишите программу вычисления арифметического выражения заданного строкой.Используйте
# операции +, -, /, *.приоритет операций стандартный.
# *Пример: *
# 2 + 2 = > 4;
# 1 + 2 * 3 = > 7;
# 1 - 2 * 3 = > -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример: *
# 1 + 2 * 3 = > 7;
# (1 + 2) * 3 = > 9;

# user_string = input("Введите число: ")
# us_str = '1+2*3'
# new_str = []
# temp = 0
# num_list = list(us_str)
# print(num_list)
# for i in range(0, len(num_list) - 1):
#     while num_list[i] == '*':
#         temp = int(num_list[i - 1]) * int(num_list[i + 1])
#         num_list.pop(i-1)
#         num_list.pop(i+1)
#         new_str.append(temp)
#     if num_list[i] == '/':
#         temp = int(num_list[i - 1]) / int(num_list[i + 1])
#         new_str.append(temp)
#     if num_list[i] == '+':
#         temp = int(num_list[i - 1]) + int(num_list[i + 1])
#         new_str.append(temp)
#     if num_list[i] == '-':
#         temp = int(num_list[i - 1]) - int(num_list[i + 1])
#         new_str.append(temp)
# print(new_str)

user_input = input('Введите выражение: ')
num_str = ''
parse = list(user_input)
print('Исходный список', parse)
while '*' in parse or '/' in parse:
    for i in range(1, len(parse) - 1):
        if parse[i] == '*':
            oper1 = int(parse.pop(i - 1))
            oper2 = int(parse.pop(i))
            parse[i - 1] = oper1 * oper2
            break
        elif parse[i] == '/':
            oper1 = int(parse.pop(i - 1))
            oper2 = int(parse.pop(i))
            parse[i - 1] = oper1 / oper2
            break
while '+' in parse or '-' in parse:
    for i in range(1, len(parse) - 1):
        if parse[i] == '+':
            oper1 = int(parse.pop(i - 1))
            oper2 = int(parse.pop(i))
            parse[i - 1] = oper1 + oper2
            break
        elif parse[i] == '-':
            oper1 = int(parse.pop(i - 1))
            oper2 = int(parse.pop(i))
            parse[i - 1] = oper1 - oper2
            break
    print(parse)

print('Конечный список', parse)

