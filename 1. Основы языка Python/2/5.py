# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.


my_list = [7, 5, 3, 3, 3]

new = int(input("Введите число: "))

if my_list[0] < new:
    my_list.insert(0, new)
elif my_list[4] > new:
    my_list.append(new)
else:
    new_list = list(set(my_list.copy()))
    new_list.append(new)
    my_list.insert(my_list.index(max(set(new_list), key=new_list.count)), new)

print(my_list)
