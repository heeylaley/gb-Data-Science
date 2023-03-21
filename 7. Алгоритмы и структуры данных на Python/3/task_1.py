# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из
# чисел в диапазоне от 2 до 9.

num_list = [2, 3, 4, 5, 6, 7, 8, 9]
count = [0, 0, 0, 0, 0, 0, 0, 0]

for el in range(2, 100):
    for num in num_list:
        if el % num == 0:
            count[num - 2] += 1

for num in num_list:
    print(f'{count[num - 2]} чис(ел/сла) кратны {num}')


# 2й вариант со словарем
#
# count = {}
#
# for i in range(2, 100):
#     for j in range(2, 10):
#         if i % j == 0:
#             count[j] = count.get(j, 0) + 1
#
# for k, v in count.items():
#     print(k, '-', v)
