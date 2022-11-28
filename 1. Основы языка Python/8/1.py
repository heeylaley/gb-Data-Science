# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class DateFormat:
    date_list = []

    @staticmethod
    def date_type(date, month, year):
        return f'{date}.{month}.{year}'

    @classmethod
    def check(cls):
        try:
            month_dict = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля',
                          8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
            a = input('Введите дату в формате "чч-мм-гг": ')
            if a.count('-') == 2:
                a = a.split('-')
                if 1 <= int(a[0]) <= 31 and len(a[0]) == 2:
                    if 1 <= int(a[1]) <= 12 and len(a[1]) == 2:
                        if 0 <= int(a[2]) <= 99 and len(a[2]) == 2:
                            ans = input('Если это ваша последняя дата для ввода введите\033[1m stop\033[0;0m: ')
                            if 'stop' in ans:
                                data = DateFormat.date_type(a[0], a[1], a[2])
                                DateFormat.date_list.append(data)
                                print(f"Последняя введённая дата: {int(a[0])} {month_dict.get(int(a[1]))} "
                                      f"'{int(a[2])} года")
                                return f'Список введённых дат: {DateFormat.date_list}'
                            else:
                                data = DateFormat.date_type(a[0], a[1], a[2])
                                DateFormat.date_list.append(data)
                                return DateFormat.check()
                        else:
                            print('Неверный формат даты. Попробуйте ещё раз')
                            return DateFormat.check()
                    else:
                        print('Неверный формат даты. Попробуйте ещё раз')
                        return DateFormat.check()
                else:
                    print('Неверный формат даты. Попробуйте ещё раз')
                    return DateFormat.check()
            else:
                print('Неверный формат даты. Попробуйте ещё раз')
                return DateFormat.check()
        except ValueError:
            print('Неверный формат даты. Попробуйте ещё раз')
            return DateFormat.check()


print(DateFormat.check())
