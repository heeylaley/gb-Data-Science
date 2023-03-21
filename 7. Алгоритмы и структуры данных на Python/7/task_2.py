# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from rand_arr import rand_arr
import operator


def merge(left, right, compare=operator.lt):
    res = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1

    return res


def merge_sort(lst, compare=operator.lt):
    if len(lst) <= 1:
        return lst

    else:
        middle = len(lst) // 2
        left = merge_sort(lst[:middle], compare)
        right = merge_sort(lst[middle:], compare)

        return merge(left, right, compare)


array = rand_arr(0, 50)
print(array)

print(merge_sort(array))
