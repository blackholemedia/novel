# -*- coding=utf-8 -*-
from algorithm.base_structure.binarytree import BinaryTree, TreeNode


class SearchTree(BinaryTree):

    def __init__(self):
        super().__init__()

    def add_node(self, data, current_node=None):
        if isinstance(data, TreeNode):
            adding_item = data
        else:
            adding_item = TreeNode(data)  # check if data is TreeNode object
        if self._is_empty():
            adding_item.parent = self._header
            self._header = adding_item
        else:
            if current_node is None:
                iter_node = self._header
            else:
                iter_node = current_node
            if data == iter_node.val:
                print('the data already exist')
            elif data > iter_node.val:
                if iter_node.right:
                    self.add_node(data, iter_node.right)
                else:
                    adding_item.parent = iter_node
                    iter_node.right = adding_item
            else:
                if iter_node.left:
                    self.add_node(data, iter_node.left)
                else:
                    adding_item.parent = iter_node
                    iter_node.left = adding_item


if __name__ == '__main__':
    import random, json

    with open("randomlist", "r", encoding='utf-8') as f:
        randomlist = json.loads(f.read())
    mysearchtree = SearchTree()
    for i in randomlist:
        mysearchtree.add_node(i)
    print(randomlist)
    mysearchtree.print_all()
