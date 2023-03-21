# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

from rand_arr import rand_arr


def bubble_sort(a):
    for n in range(1, len(a)):
        for i in range(len(a) - n):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]


array = rand_arr(-100, 100)
print(array)

bubble_sort(array)
print(array)
