# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


a = int(input("n = "))

b = str(a)

print(f"n + nn + nn = {b * 3}")
