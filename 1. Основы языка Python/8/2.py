# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class Division:
    @staticmethod
    def div_func():
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            res = round(a / b, 2)
            return res
        except ValueError:
            print("Введите правильные данные (Нужно ввести\033[1m число\033[0;0m)")
            return Division.div_func()
        except ZeroDivisionError:
            print("Введите правильные данные (Второе число не может быть =\033[1m 0\033[0;0m)")
            return Division.div_func()


print(Division.div_func())
