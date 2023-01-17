# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#  *Пример:*
#  [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# вариант 1:
num_list = [1, 2, 3, 5, 1, 5, 3, 10]
new_list = []
for i in num_list:
    if num_list.count(i)==1:
        new_list.append(i)

print(new_list)

# вариант 2:
my_list = [1, 2, 3, 5, 1, 5, 3, 10]
my_dict = {}
for item in my_list:
    my_dict[item] = my_dict.get(item, 0)+1
print(my_dict)
for key, value in my_dict.items():
    if value == 1:
        print(key)

# вариант 3
data = [1, 2, 3, 5, 1, 5, 3, 10]
proverka = lambda x: data.count(x) == 1
new_data = filter(proverka, data)
new_data = list(new_data)
print(new_data)

# или
print([x for x in my_list if my_list.count(x) == 1])