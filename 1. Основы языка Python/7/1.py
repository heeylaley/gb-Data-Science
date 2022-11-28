# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.


class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        res_matrix = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        for i in range(len(self.list_1)):
            for j in range(len(self.list_2)):
                res_matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return res_matrix

    def __str__(self):
        res = Matrix.__add__(self)
        print(str('\n'.join(['\t'.join([str(j) for j in i]) for i in res])))


my_matrix = Matrix([[10, 100, 13],
                    [-2, 42, 772],
                    [3, 30, 73]], [[2, 2, 70],
                                   [2, 8, 228],
                                   [0, 0, 0]])
my_matrix.__str__()
