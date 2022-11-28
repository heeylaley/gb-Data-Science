# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.



from abc import ABC, abstractmethod


class WareHouse:
    a_unit = []
    b_unit = []
    c_unit = []

    @staticmethod
    def check():
        def unit_print(unit_list):
            for el in unit_list:
                print(el)
        ans = input('Если хотите посмотреть склад введите\033[1m check\033[0;0m: ')
        if 'check' in ans:
            print('Юнит склада "A" пустой') if WareHouse.a_unit == [] else \
                print('ЮНИТ "А":'), unit_print(WareHouse.a_unit)
            print('Юнит склада "B" пустой') if WareHouse.b_unit == [] else \
                print('ЮНИТ "B":'), unit_print(WareHouse.b_unit)
            print('Юнит склада "C" пустой') if WareHouse.c_unit == [] else \
                print('ЮНИТ "C":'), unit_print(WareHouse.c_unit)
        else:
            return 'Склад закрыт'

    @classmethod
    def appending(cls, name, price, quantity_prev, markup):
        try:
            quantity_new = int(input('Введите количество товара, которое вы хотите перевести на склад: '))
            if 0 <= quantity_new <= quantity_prev:
                unit = input('Укажите юнит склада (заглавной\033[1m английской\033[0;0m буквой A, B или C): ')
                if len(unit) != 1:
                    print('Юнит склада указан неверно')
                    return WareHouse.appending(name, price, quantity_prev, markup)
                else:
                    if 'A' == unit:
                        print('Переведено на склад А')
                        WareHouse.a_unit.append({'Наименование': name, 'Цена': price,
                                                 'Количество на складе': quantity_new, 'Наценка': markup})
                    elif 'B' == unit:
                        print('Переведено на склад B')
                        WareHouse.b_unit.append({'Наименование': name, 'Цена': price,
                                                 'Количество на складе': quantity_new, 'Наценка': markup})
                    elif 'C' == unit:
                        print('Переведено на склад C')
                        WareHouse.c_unit.append({'Наименование': name, 'Цена': price,
                                                 'Количество на складе': quantity_new, 'Наценка': markup})
                    else:
                        print('Юнит склада указан неверно')
                        return WareHouse.appending(name, price, quantity_prev, markup)
            else:
                print('Указано неверное количество')
                return WareHouse.appending(name, price, quantity_prev, markup)
        except ValueError:
            print('Указано неверное количество')
            return WareHouse.appending(name, price, quantity_prev, markup)


class Techs(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self._markup = 1.1
        self.value = self._markup * price

    @abstractmethod
    def description(self):
        return f'Производственная информация о {self.name}'

    def __str__(self):
        return f'{self.name.upper()} \nЦена за шт. = {self.price} \nКоличество = {self.quantity} шт.'

    def to_w_house(self):
        return WareHouse.appending(self.name, self.price, self.quantity, self._markup)


class Printer(Techs):
    def __init__(self, name, price, quantity):
        self._markup = 1.5
        super().__init__(name, price, quantity)

    def description(self):
        return f"Максимальное время ожидания {self.name} на складе: 1 неделя \n" \
               f"Доп функционал: инструкция, картридж, чернила, кабель \n" \
               f"Примерная выручка в этом месяце = {self.value * self.quantity} \n" \
               f"Гейт отгрузки: 1082"


class Scanner(Techs):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self._markup = 1.25

    def description(self):
        return f"Максимальное время ожидания {self.name} на складе: 1 неделя \n" \
               f"Доп функционал: инструкция, матрица, кабель \n" \
               f"Примерная выручка в этом месяце = {self.value * self.quantity} \n" \
               f"Гейт отгрузки: 133"


class Copier(Techs):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self._markup = 1.33

    def description(self):
        return f"Максимальное время ожидания {self.name} на складе: 1 неделя \n" \
               f"Доп функционал: инструкция, картридж, чернила, кабель \n" \
               f"Примерная выручка в этом месяце = {self.value * self.quantity} \n" \
               f"Гейт отгрузки: 980"


hp_330 = Printer('Принтер hp модель 3.3.0', 300, 45)
kyocera = Copier('Ксерокс kyocera', 250, 32)
canon_550 = Scanner('Сканер canon поколение 5 версия 5.0', 275, 140)
hp_2S = Printer('Принтер hp модель 2S', 500, 15)
kyocera_2 = Copier('Ксерокс kyocera версия 2.0', 300, 10)
canon_530 = Scanner('Сканер canon поколение 5 версия 3.0', 250, 50)

print(hp_330)
print(hp_330.description())
print(kyocera)
print(kyocera.description())
print(canon_550)
print(canon_550.description())

hp_330.to_w_house()
hp_2S.to_w_house()
kyocera.to_w_house()
kyocera_2.to_w_house()
canon_530.to_w_house()
canon_550.to_w_house()
WareHouse.check()
