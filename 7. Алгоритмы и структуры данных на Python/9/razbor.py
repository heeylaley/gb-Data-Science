import heapq  # модуль для работы с приоритетной очередью
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):  # класс Узел, имеет потомков - Левый и Правый
    def walk(self, code, acc):  # функция обхода по узлам. В acc накапливаем значение кода
        # (влево - 0, вправо - 1) для символа, пока не дойдем до Листа
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):  # класс Лист, с аттрибутом - Символ
    def walk(self, code, acc):
        code[self.char] = acc or "0"  # записываем в словарь значение символа и его накопленный код (путь от вершины)


def huffman_encode(s):  # функция возвращает словарь с символом в качестве ключа, и его кода в качестве значения
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))  # заполняем список кортежами (частота, уникальное значение, класс Лист со
        # значением символа )

    heapq.heapify(h)  # помещаем наш список кортежей в приоритетную очередь. Приоритет в первой позиции кортежа

    count = len(h)
    while len(h) > 1:  # построение дерева Хаффмана, в листьях которого будут содержатся символы,
        # в узлах - приоритет (вес) узла.
        freq1, _count1, left = heapq.heappop(h)  # разгужаем и удаляем первый элемент с наименьшим приоритетом
        freq2, _count2, right = heapq.heappop(h)  # разгужаем и удаляем второй элемент с наименьшим приоритетом

        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))  # вставляем узел в приоритетную очередь
        count += 1

    code = {}
    if h:  # если очередь пустая (строка на входе - пустая, то делать ytxtuj
        [(_freq, _count, root)] = h  # root - корень дерева Хаффмана
        root.walk(code, "")  # обходим дерево и формируем наш словарь с символами и кодами
    return code


s = input('Введите строку: ')
# s = 'beep boop beer!'
code = huffman_encode(s)
print(f'Словарь с кодами символов {code}')

encoded = "".join(code[ch] for ch in s)
print('Таблица кодирования Хаффмана:')
for ch in code:
    print(f'{ch}:{code[ch]}')
print(f'Количество символов в строке: {len(s)}. Длина строки в ASCII кодировке: {len(s) * 8}')
print(f'Всего уникальных символов: {len(code)}. Длина закодированной строки: {len(encoded)}')
print(f'Закодированная строка:  {encoded}')
