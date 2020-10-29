from custom_profiler.custom_profiler import custom_line_profiler


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
