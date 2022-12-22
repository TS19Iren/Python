# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,-13, -8, -5, −3, -2, −1, -1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

user_number = int(input('Введите число: '))


def findingFibonachi(number):
    fibbo_list = [0, 1]

    for i in range(2, number + 1):
        fibbo_list.append(fibbo_list[i - 2] + fibbo_list[i - 1])
    return (fibbo_list)

def reverse_list(my_list):
    new_list = []
    for i in range(len(my_list)-1, 1, -1):
        new_list.append(-1 * my_list[i])
    return new_list
def merge_list(left_list,right_list):
    for i in right_list:
        left_list.append(i)
    return left_list

right_list = findingFibonachi(user_number)
left_list = reverse_list(right_list)
print(merge_list(left_list, right_list))

