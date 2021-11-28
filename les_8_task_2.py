"""
Задача 2. Закодируйте любую строку по алгоритму Хаффмана.
Превратите строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных.
"""

from collections import Counter


class NodeHuff:
    def __init__(self, sym: str, freq: int, left=None, right=None):
        self.sym = sym
        self.freq = freq
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.sym}: {self.freq}, left: {self.left}, right: {self.right}'


class TreeHuff:
    def __init__(self):
        self.nodes = []

    def add_node(self, node: NodeHuff):
        self.nodes.append(node)

    def search_node(self, s_st: str):
        for obj in self.nodes:
            if obj.sym == s_st:
                return obj

    def get_code(self, search_sym: str):
        node = self.nodes[-1]
        path = ''
        while node.left and node.right:
            left = node.left
            right = node.right
            if search_sym in left.sym:
                path += '0'
                node = node.left
            if search_sym in right.sym:
                path += '1'
                node = node.right
        return path


def huff_algo(st_str: str):
    freq_table = Counter(st_str)
    tree_huff = TreeHuff()

    while len(freq_table) > 1:
        left = freq_table.most_common()[-1]
        right = freq_table.most_common()[-2]
        freq_table.pop(left[0])
        freq_table.pop(right[0])
        if len(left[0]) == 1:
            left = NodeHuff(left[0], left[1])
        else:
            left = tree_huff.search_node(left[0])
        if len(right[0]) == 1:
            right = NodeHuff(right[0], right[1])
        else:
            right = tree_huff.search_node(right[0])
        tree_huff.add_node(left)
        tree_huff.add_node(right)
        top = NodeHuff(str(left.sym + right.sym), int(left.freq + right.freq), left, right)
        tree_huff.add_node(top)
        freq_table[top.sym] = top.freq

    freq_table = Counter(st_str).keys()
    code_sym = dict()
    for key in freq_table:
        code_sym[key] = tree_huff.get_code(key)
    result = ''
    for s in st_str:
        result += code_sym[s]
    return result


beep = 'beep boop beer!'
test_str = 'Это тестовая строка для проверки алгоритма Хаффмана'
print(huff_algo(beep))
print(huff_algo(test_str))
