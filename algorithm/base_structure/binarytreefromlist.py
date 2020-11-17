# -*- coding=utf-8 -*-
# this is for creating a binary tree from a list. The only difference with binarytree is the add_node method

import random
from algorithm.base_structure.binarytree import BinaryTree, TreeNode


class BinaryTreeFromList(BinaryTree):

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
            if iter_node.left is None:
                adding_item.parent = iter_node
                iter_node.left = adding_item
            elif iter_node.right is None:
                adding_item.parent = iter_node
                iter_node.right = adding_item
            else:
                if iter_node.left.val == "#":
                    self.add_node(data, iter_node.right)
                elif iter_node.right.val == "#":
                    self.add_node(data, iter_node.left)
                elif random.randint(0, 999) % 2 == 0:
                    self.add_node(data, iter_node.left)
                else:
                    self.add_node(data, iter_node.right)

    def add_node_byleft(self, data, current_node=None):
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
            if iter_node.left is None:
                adding_item.parent = iter_node
                iter_node.left = adding_item
            elif iter_node.right is None:
                adding_item.parent = iter_node
                iter_node.right = adding_item
            else:
                if iter_node.left.val == "#":
                    self.add_node_byleft(data, iter_node.right)
                elif iter_node.right.val == "#":
                    self.add_node_byleft(data, iter_node.left)
                elif iter_node.left.left and iter_node.left.right:
                    if iter_node.right.left and iter_node.right.right:
                        self.add_node_byleft(data, iter_node.left)
                    else:
                        self.add_node_byleft(data, iter_node.right)
                else:
                    self.add_node_byleft(data, iter_node.left)

    def dec_alergic(self, root=None):
        if root:
            if root.left is None:
                pass
            elif root.left.val == '#':
                root.left = None
            else:
                self.dec_alergic(root.left)
            if root.right is None:
                pass
            elif root.right.val == '#':
                root.right = None
            else:
                self.dec_alergic(root.right)
        else:
            self.dec_alergic(self._header)


if __name__ == '__main__':
    '''
    import random,json
    with open("randomlist","r",encoding='utf-8') as f:
        randomlist = json.loads(f.read())
    '''
    mybinarytree = BinaryTreeFromList()
    for i in [5, 4, '#', 3, '#', 2]:
        mybinarytree.add_node(i)
    mybinarytree.print_all()
    mybinarytree.dec_alergic()
    mybinarytree.print_all()
