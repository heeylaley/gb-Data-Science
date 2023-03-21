# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

num = input('Введите числа через пробел: ')
num = num.split(' ')

# 2й вариант:
# n = int(input('Введите количество натуральных чисел: '))
# nums = [input(f'Введите {i + 1}-е число: ') for i in range(n)]

while len(num) != 1:
    if int(num[0]) > int(num[1]):
        num.remove(num[1])
    else:
        num.remove(num[0])

num_sum = sum(map(int, num[0]))

print(f'наибольшее число - {num[0]}, сумма цифр = {num_sum}')
