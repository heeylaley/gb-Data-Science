# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем. Об окончании ввода данных свидетельствует пустая строка.


def input_text(a):
    text = []
    f_obj = open(a, 'w+', encoding='utf-8')

    def loop():
        the_line = input('Введите текст (Если хотите завершить нажмите Enter): ')
        if the_line != '':
            text.append(the_line)
            text.append('\n')
            return loop()
        else:
            f_obj.writelines(text)
            f_obj.seek(0)
            print(f_obj.read())
            f_obj.close()

    loop()


input_text('text_1.txt')
