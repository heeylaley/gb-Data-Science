# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a
# километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее
# b километров. Программа должна принимать значения параметров a и b и выводить одно
# натуральное число — номер дня.


a = float(input("Ваш ежедневный результат в км: "))

b = float(input("Ваш желаемый результат в км: "))

day = 0

while a < b:
    day += 1
    a = 1.1*a

print(f"При ежедневном приросте дистанции в 10% вам понадобится {day} дня(-дней)")
