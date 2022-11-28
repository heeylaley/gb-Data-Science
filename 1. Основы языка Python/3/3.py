# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


from functools import reduce

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

max_sum = reduce(lambda x, y: y if (x < y) else x, [a + b, b + c, a + c])

print(max_sum)
