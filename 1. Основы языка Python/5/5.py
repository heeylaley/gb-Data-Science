# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def to_digits(a):
    num_list = []
    for el in a:
        if el.isdigit() or el.replace('-', '').isdigit():
            num_list.append(int(el))
        elif el.replace('.', '').isdigit():
            num_list.append(float(el))
        else:
            del el
    return num_list


with open("text_5.txt") as f_obj:
    text = f_obj.read().split()
    int_text = to_digits(text)
    print(sum(int_text))
