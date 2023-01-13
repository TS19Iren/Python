# В файле находится N натуральных чисел, записанных через пробел.
# # Среди чисел не хватает одного, чтобы выполнялось условие
# # A[i] - 1 = A[i-1]. Найдите это число.

data = '1 2 3 4 5 6 8 9 11'
new_data = list(map(int,data.split()))
print(new_data)
for i in range(len(new_data)-1):
    if not new_data[i]+1 == new_data[i+1]:
        print(new_data[i]+1)
# my_func = list(filter(lambda i: not data[i] + 1 == data[i + 1], range(len(data) - 1)))
#
# for item in my_func:
#     print(data[item] + 1)
