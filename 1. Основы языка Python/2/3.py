# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.


dict_year = dict(зима=[1, 2, 12], весна=[3, 4, 5], лето=[6, 7, 8], осень=[9, 10, 11])
list_year = ["зима", "весна", "лето", "осень"]

month = int(input("Введите месяц (от 1 до 12): "))

if month > 12:
    print("Ошибка ввода")
else:
    for el in dict_year:
        tern_op = print(f"Через dict. Время года - {el}") if month in list(dict_year.get(el)) else False

    if month in (1, 2, 12):
        print(f"Через list. Время года - {list_year[0]}")
    elif month in (3, 4, 5):
        print(f"Через list. Время года - {list_year[1]}")
    elif month in (6, 7, 8):
        print(f"Через list. Время года - {list_year[2]}")
    else:
        print(f"Через list. Время года - {list_year[3]}")
