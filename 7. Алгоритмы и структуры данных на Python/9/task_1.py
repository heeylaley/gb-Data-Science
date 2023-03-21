# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.

from hashlib import sha1
from itertools import combinations


def substring(a):
    if a == '':
        return 0

    hash_set = set()

    for i in range(len(a) - 1):
        for j in range(i + 1, len(a) + 1):
            hash_set.add(hash(a[i:j]))

    return len(hash_set) - 1


hash_str = input('Введите строку: ')
print(f'Количество подстрок в вашей строке = {substring(hash_str)}')
