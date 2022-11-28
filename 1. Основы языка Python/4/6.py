# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.


from itertools import cycle
from itertools import count

for el in count(3, 2):
    if el > 10:
        break
    else:
        print(el)

# б
c = 0
for el in cycle([23, 'lalala']):
    if c > 10:
        break
    else:
        print(el)
        c += 1
