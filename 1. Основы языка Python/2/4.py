# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.


my_str = input("Введите предложение: ")

words = list(my_str.split())

for el in words:
    print(words.index(el) + 1, el.title()[0: 11])
