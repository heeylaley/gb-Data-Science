# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?

import numpy as np

n = int(input('Количество друзей: '))
a = np.zeros((n, n))

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        a[i][j] += 1

print(f'Количество рукопожатий = {round(np.sum(a))}')
