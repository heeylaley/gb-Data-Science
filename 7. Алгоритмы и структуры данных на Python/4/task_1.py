# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков.
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы
# проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

import cProfile


# Алгоритм из задания 3.1
# 1й вариант (мой)
def mult_count_1():
    num_list = [2, 3, 4, 5, 6, 7, 8, 9]
    count = [0, 0, 0, 0, 0, 0, 0, 0]

    for el in range(2, 1_000_000):
        for num in num_list:
            if el % num == 0:
                count[num - 2] += 1

    for num in num_list:
        print(f'{count[num - 2]} чис(ел/сла) кратны {num}')


# 2й вариант
def mult_count_2():
    num_2 = num_3 = num_4 = num_5 = num_6 = num_7 = num_8 = num_9 = 0

    for el in range(2, 1000000):
        if el % 2 == 0:
            num_2 += 1
        if el % 3 == 0:
            num_3 += 1
        if el % 4 == 0:
            num_4 += 1
        if el % 5 == 0:
            num_5 += 1
        if el % 6 == 0:
            num_6 += 1
        if el % 7 == 0:
            num_7 += 1
        if el % 8 == 0:
            num_8 += 1
        if el % 9 == 0:
            num_9 += 1

    print(f'{num_2} чис(ел/сла) кратны 2')
    print(f'{num_3} чис(ел/сла) кратны 3')
    print(f'{num_4} чис(ел/сла) кратны 4')
    print(f'{num_5} чис(ел/сла) кратны 5')
    print(f'{num_6} чис(ел/сла) кратны 6')
    print(f'{num_7} чис(ел/сла) кратны 7')
    print(f'{num_8} чис(ел/сла) кратны 8')
    print(f'{num_9} чис(ел/сла) кратны 9')


# 3й вариант
def mult_count_3():
    multiplicity = {i: 0 for i in range(2, 10)}

    for val in range(2, 1000000):
        for key in multiplicity.keys():
            multiplicity[key] += 1 if val % key == 0 else 0

    for el in multiplicity:
        print(f'{multiplicity.get(el)} чис(ел/сла) кратны {el}')


# 1
# cProfile.run('mult_count_1()')
#
# 100 loops, best of 5: 27 nsec per loop
#
# 12 function calls in 0.845 seconds


# 2
# cProfile.run('mult_count_2()')
#
# 100 loops, best of 5: 22 nsec per loop
#
# 12 function calls in 0.575 seconds


# 3
# cProfile.run('print(mult_count_3())')
#
# 100 loops, best of 5: 25 nsec per loop
#
# 1000019 function calls in 2.068 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 999998    0.114    0.000    0.114    0.000 {method 'keys' of 'dict' objects}


# Вывод: наблюдается обратная зависимость между объёмом функции и ввременем её выполнения
# Самый лаконичный код выполняется дольше всех (из-за работы со словарём методом keys())
# Самый объёмный код выполняется быстрее всего тк без дополнительных списков/словарей проверяет кратность ренджа
# Ну а мой посерединке)
