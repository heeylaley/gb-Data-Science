# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# без применения set()  (аналог sorted())

from random import sample

num_list = sample(range(30), 10)
print(num_list)

max_num = min_num = num_list[0]

for num in num_list:
    if num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num

max_ind = num_list.index(max_num)
min_ind = num_list.index(min_num)

num_list[max_ind], num_list[min_ind] = num_list[min_ind], num_list[max_ind]

print(num_list)
