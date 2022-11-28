# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на
# экран.


class FriendsList:
    friends_list = dict({})

    @classmethod
    def acq(cls):
        friend_name = input("Введи имя своего друга: ")
        try:
            age = int(input(f'"{friend_name}", запомнил! А теперь введи его/её возраст: '))
            if age > 100:
                print("Так я и поверил")
                print("Попробуй ещё раз")
                return FriendsList.acq()
            elif age < 0:
                print("Отрицательный возраст - это что-то новенькое!")
                print("Попробуй ещё раз")
                return FriendsList.acq()
            else:
                FriendsList.friends_list.update({friend_name: f'{age} года/лет'})
                print('Хорошо! :^)')
                ans = input('Если ты закончил введи\033[1m stop\033[0;0m: ')
                if 'stop' in ans:
                    for el in FriendsList.friends_list:
                        print(f'Имя - {el}, возраст - {FriendsList.friends_list.get(el)}')
                else:
                    return FriendsList.acq()
        except ValueError:
            print('Возраст должен быть числом (и без знаков после запятой)!')
            return FriendsList.acq()


FriendsList.acq()
