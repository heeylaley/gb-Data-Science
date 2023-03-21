# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

from random import sample

num_list = sample(range(30), 10)
print(num_list)

min_num_1 = num_list[0]
min_num_2 = num_list[1]

for num in num_list:
    if num_list.index(num) > 0:
        if num < min_num_1:
            min_num_2 = min_num_1
            min_num_1 = num
        elif min_num_1 <= num < min_num_2:
            min_num_2 = num

print(f'Минимальные числа: \n{min_num_1} \n{min_num_2}')
