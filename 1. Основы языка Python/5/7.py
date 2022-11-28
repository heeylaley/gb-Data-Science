# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]


import json

dict_firm = {}
dict_profit = {}
res_profit = 0
aver_prof = 0
i = 0

with open(r"C:\Users\Катя\Desktop\text_7.txt", encoding='utf-8') as f_obj:

    for line in f_obj:
        name, f_type, earning, damage = line.split()
        profit = int(earning) - int(damage)
        dict_firm.update({name: profit})
        if profit >= 0:
            res_profit = res_profit + profit
            i += 1
        else:
            res_profit = res_profit + 0

    if i != 0 and res_profit != 0:
        aver_prof = res_profit / i
        print(f'Средняя прибыль = {round(aver_prof)}')
    elif res_profit == 0 and i != 0:
        print('Все фирмы выходят в ноль')
    else:
        print('Все фирмы работают в убыток')

    dict_profit = {'средняя прибыль': round(aver_prof)}
    print(dict_firm)

with open('text_7.json', 'w', encoding='utf-8') as j_obj:
    json.dump(dict_profit, j_obj, ensure_ascii=False)
    json.dump(dict_firm, j_obj, ensure_ascii=False)
