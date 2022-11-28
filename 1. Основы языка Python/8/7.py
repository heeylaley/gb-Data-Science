# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b < 0:
            return f'n = {self.a} - {abs(self.b)}i'  # сделала abs() потому что без пробелов выглядело не очень красиво
        else:
            return f'n = {self.a} + {self.b}i'

    def __add__(self, other):
        return f'n_1 + n_2 = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'n_1 x n_2 = {self.a * other.a - (self.b * other.b)} + {self.a * other.b + other.a * self.b}i'


n_1 = ComplexNum(1, -2)
n_2 = ComplexNum(-3, 5)
print(n_1)
print(n_1 + n_2)
print(n_1 * n_2)
