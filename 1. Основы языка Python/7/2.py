# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это
# могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для
# костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod
res_sum = []


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calc_square(self):
        return f'Площадь материала для {self.name} = '


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
        self.square = self.size / 6.5 + 0.5
        res_sum.append(self.square)  # примечательно что питон не ругается на переменную res_sum

    @property
    def composition(self):
        return f'Состав {self.name}: 100% шерсть'

    def calc_square(self):
        return f'Расход ткани на {self.name} = {self.square}'


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height
        self.square = self.height * 2 + 0.3
        res_sum.append(self.square)

    @property
    def composition(self):
        return f'Состав {self.name}a: 100% хлопок'

    def calc_square(self):
        return f'Расход ткани на {self.name} = {self.square}'


coat_1 = Coat('1 пальто', 52)
coat_2 = Coat('2 пальто', 40)
suit_1 = Suit('1 костюм', 183)
suit_2 = Suit('2 костюм', 167)
print(coat_1.calc_square())
print(suit_1.calc_square())
print(coat_2.composition)
print(suit_2.composition)
print(f'Общий расход ткани на всю одежду = {round(sum(res_sum), 2)}')
