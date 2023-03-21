# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5

from random import sample

num_list = sample(range(30), 10)
ind_list = [num_list.index(el) for el in num_list if el % 2 == 0]

print(num_list)
print(ind_list)
