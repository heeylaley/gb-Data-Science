# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.


p_str = input("Введите числа через пробел (символ \033[1mQ\033[0;0m = остановка): ").split()
res = 0


def to_digits(a):
    num_list = []
    for el in a:
        if el.isdigit() or el.replace('-', '').isdigit():
            num_list.append(int(el))
        elif el.replace('.', '').isdigit():
            num_list.append(float(el))
        else:
            del el  # не уверена что конкретно такая запись правильна, но ничего лучше не придумала
    if res == 0:
        return num_list
    else:
        num_list.append(res)
    return num_list


def list_sum(b):
    if 'Q' in b:
        new_list = []
        for el in b:
            if b.index(el) < b.index('Q'):
                new_list.append(el)
        numbers = to_digits(new_list)
    else:
        numbers = to_digits(b)
    return sum(numbers)


def cycle_func(c):
    global res
    res = list_sum(c)
    print(f'Сумма = {res}.')
    new_el = input('Если хотите завершить введите "Нет". Введите новые элементы для суммы если хотите продолжить: '
                   '').split()
    if 'Нет' in new_el:
        return f'Окончательная сумма = {res}.'
    else:
        new_list = []
        for el in new_el:
            new_list.append(el)
        return cycle_func(new_list)


print(cycle_func(p_str))
