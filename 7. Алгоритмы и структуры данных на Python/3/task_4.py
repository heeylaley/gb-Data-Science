# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

num_list = [randint(1, 5) for i in range(10)]
print(num_list)

num_freq = {}

for el in num_list:
    if el in num_freq:
        num_freq[el] += 1
    else:
        num_freq[el] = 1

max_freq = 1

for el in num_freq.keys():
    if num_freq.get(el) > max_freq:
        max_freq = num_freq.get(el)
        max_el = el

print(f'Число {max_el} встречается {max_freq} раз(-a)')
