# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.

from rand_arr import rand_arr
from random import choice
from statistics import median


def med_search(a, medd):
    pivot = choice(a)

    left = [el for el in a if el < pivot]
    right = [el for el in a if el > pivot]
    meds = [el for el in a if el == pivot]

    if medd < len(left):
        return med_search(left, medd)
    elif medd < len(left) + len(meds):
        return meds[0]
    else:
        return med_search(right, medd - len(left) - len(meds))


array = rand_arr(0, 100)
print(array)
print(median(array))  # вообще можно было обойтись этой функцией, так как правилам задания median() не противоречит))0
# но оставим просто в качестве проверки

print(f'медиана массива = {med_search(array, len(array) // 2)}')
