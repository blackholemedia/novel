from custom_profiler.custom_profiler import custom_line_profiler

BLANK = ' ' * 4
SLASH = '-' * 4


class Tree(object):

    @custom_line_profiler
    def get(self):
        pass


class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value) if self.value else ''


class BinarySearchTree(object):

    def __init__(self):
        self.root = Node()
        super().__init__()

    def __repr__(self):
        return self.root

    def _find_max(self, node):
        if not node:
            return None
        else:
            if not node.right:
                return node
            else:
                return self._find_max(node.right)

    def find_max(self):
        if not self.root.value:
            print('The tree is empty, nothing to do')
            return
        return self._find_max(self.root)

    def _find_min(self, node):
        if not node:
            return None
        else:
            if not node.left:
                return node
            else:
                return self._find_min(node.left)

    def find_min(self):
        if not self.root.value:
            print('The tree is empty, nothing to do')
            return
        return self._find_min(self.root)

    def _reverse_infix_print(self, node, depth, on_right=True):
        if not node:
            return None
        else:
            self._reverse_infix_print(node.right, depth + 1)
            if on_right:
                if node.right or node.left:
                    print(BLANK * depth + str(node) + SLASH)
                else:
                    print(BLANK * depth + str(node))
                # print((BLANK * depth + '|\n') * 2 + BLANK * depth + '|')
            else:
                print((BLANK * (depth - 1) + '|' + BLANK + '|\n') * 2 + (BLANK * (depth - 1) + '|' + BLANK + '|'))
                # print((' ' * 4 * depth + '|\n') * 2 + ' ' * 4 * depth + '|')
                if node.right or node.left:
                    print(BLANK * depth + str(node) + SLASH)
                else:
                    print(BLANK * depth + str(node))
            self._reverse_infix_print(node.left, depth + 1, on_right=False)

    def reverse_infix_print(self):
        if not self.root:
            print('The tree is EMPTY')
        else:
            self._reverse_infix_print(self.root.right, depth=1)
            print(str(self.root) + '-' * 4)
            self._reverse_infix_print(self.root.left, depth=1, on_right=False)

    def _insert(self, node, value):
        if node.value == value:
            print('Node already exists, nothing to do')
            return
        elif node.value > value:
            if not node.left:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if not node.right:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def insert(self, value):
        if not self.root.value:
            self.root.value = value
        else:
            self._insert(self.root, value)


if __name__ == '__main__':
    rec = BinarySearchTree()
    a = rec.find_max()
    if a:
        print(a)
    for i in [3, 1, 4, 6, 9, 2, 5, 7]:
        rec.insert(i)
    print(rec.root)
    b = rec.find_min()
    if b:
        print(b)
    # rec.reverse_infix_print()
