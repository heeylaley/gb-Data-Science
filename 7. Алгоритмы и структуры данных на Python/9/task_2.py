# 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter, OrderedDict


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class Leaf:
    def __init__(self, symbol: str, value: int):
        self.symbol = symbol
        self.value = value


class Huffman:
    tree: list

    def __init__(self):
        self.code = dict()
        self.tree = []
        self.text = ''

    def leaf_list(self, a):
        counter = dict(Counter(a))
        counter = OrderedDict(sorted(counter.items(), key=lambda k: k[1], reverse=True))

        for symbol, value in counter.items():
            self.tree.append(Leaf(symbol, value))

        return True

    def huff_leaf(self):
        try:
            while len(self.tree) > 2:
                b, a = self.tree.pop(), self.tree.pop()
                spam = Node(a.value + b.value, a, b)

                if spam.value >= self.tree[0].value:
                    self.tree.insert(0, spam)
                elif spam.value < self.tree[-1].value:
                    self.tree.append(spam)
                else:
                    for i in range(1, len(self.tree)):
                        if self.tree[i - 1].value >= spam.value > self.tree[i].value:
                            self.tree.insert(i, spam)
                            break

            self.tree = Node(self.tree[0].value + self.tree[1].value, self.tree[0], self.tree[1])

        except IndexError or self.tree == []:
            print('Ваша строчка должна содержать не меньше 2 разных символов!')

    def huff_recursion(self, data, code=''):
        if isinstance(data, Node):
            self.huff_recursion(data.left, code=code + '0')
            self.huff_recursion(data.right, code=code + '1')
        elif isinstance(data, Leaf):
            self.code[data.symbol] = code

    def _encode(self):
        res = []

        for el in self.text:
            res.append(self.code[el])

        return ''.join(res)

    def encode(self, b):
        self.__init__()
        self.text = b
        self.leaf_list(b)
        self.huff_leaf()
        self.huff_recursion(self.tree)
        res = self._encode()

        return res

    def get_table(self):
        return self.code


txt = input('Введите строку: ')
huff = Huffman()

print('Результат кодирования:')
print(huff.encode(txt))
print('Таблица кодирования:')
print(huff.get_table())
