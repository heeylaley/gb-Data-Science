# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим
# очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n). Функция
# отвечает за получение факториала числа, а в цикле необходимо выводить только
# первые n чисел, начиная с 1! и до n!.


from math import factorial


def fact(n):
    generator = [num + 1 for num in range(n)]
    for el in generator:
        yield el


for i in fact(7):
    print(factorial(i))
