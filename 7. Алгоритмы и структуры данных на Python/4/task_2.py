# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
# улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».

import cProfile


# 1. с применением решета Эратосфена
def erat(n, mult):
    try:
        sieve = [i for i in range(mult * n + 1)]
        sieve[1] = 0

        for i in range(2, mult * n + 1):
            if sieve[i] != 0:
                j = i * 2

                while j <= mult * n:
                    sieve[j] = 0
                    j += i

        simples = [i for i in sieve if i != 0]

        return simples[n - 1]

    except IndexError:
        return erat(n, mult + 1)


# 2. без применения решета Эратосфена
def non_erat(n, mult):
    try:
        simples = []

        for i in range(2, mult * n + 1):
            for j in simples:
                if i % j == 0:
                    break
            else:
                simples.append(i)

        return simples[n - 1]

    except IndexError:
        return non_erat(n, mult + 1)


#   erat
# for el in range(900, 1000):
#     print(f'{el} простое число = {erat(el, 5)}')
# 100 loops, best of 5: 29 nsec per loop

# cProfile.run('erat(1000, 4)')
# 18 function calls (14 primitive calls) in 0.018 seconds


#   non_erat
# for el in range(900, 1000):
#     print(f'{el} простое число = {non_erat(el, 5)}')
# 100 loops, best of 5: 13 nsec per loop

# cProfile.run('non_erat(1000, 4)')
# 3917 function calls (3913 primitive calls) in 0.134 seconds


# Вывод: non_erat медленнее (тормозит append())
