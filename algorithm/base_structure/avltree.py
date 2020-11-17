# -*- coding=utf-8 -*-

from algorithm.base_structure.searchtree import SearchTree
from algorithm.base_structure.binarytree import TreeNode


class AvlTreeNode(TreeNode):
    def __init__(self, item=None, height=None):
        super().__init__(item)
        self._height = height


class AvlTree(SearchTree):

    def __init__(self):
        super().__init__()

    def height(self, tree=None):
        if tree is None:
            return -1
        else:
            return tree._height

    def SingleRotateWithLeft(self, k1=None, k2=None):
        k1.parent = k2.parent
        k2.left = k1.right
        k1.right = k2
        k2.parent = k1
        if k1.val < k1.parent.val:
            k1.parent.left = k1
        else:
            k1.parent.right = k1
        if k2.left is not None:
            k2.left.parent = k2
        k1._height = max(self.height(k1.left), self.height(k1.right)) + 1
        k2._height = max(self.height(k2.left), self.height(k2.right)) + 1
        return k1

    def SingleRotateWithRight(self, k1=None, k2=None):
        k2.parent = k1.parent
        k1.right = k2.left
        k2.left = k1
        k1.parent = k2
        if k2.val < k2.parent.val:
            k2.parent.left = k2
        else:
            k2.parent.right = k2
        if k1.right is not None:
            k1.right.parent = k1
        k1._height = max(self.height(k1.left), self.height(k1.right)) + 1
        k2._height = max(self.height(k2.left), self.height(k2.right)) + 1
        return k2

    def DoubleRotateWithLeft(self, k1=None, k2=None, k3=None):
        self.SingleRotateWithRight(k1, k2)
        self.SingleRotateWithLeft(k2, k3)
        k1._height = max(self.height(k1.left), self.height(k1.right)) + 1
        k3._height = max(self.height(k3.left), self.height(k3.right)) + 1
        return k2

    def DoubleRotateWithRight(self, k1=None, k2=None, k3=None):
        self.SingleRotateWithLeft(k2, k3)
        self.SingleRotateWithRight(k1, k2)
        k1._height = max(self.height(k1.left), self.height(k1.right)) + 1
        k3._height = max(self.height(k3.left), self.height(k3.right)) + 1
        return k2

    def add_node(self, data, parent_node=None, current_node=None):
        if self._is_empty():
            if isinstance(data, AvlTreeNode):  # check if data is AVLTreeNode
                adding_item = data
            else:
                adding_item = AvlTreeNode(data)  # check if data is AVLTreeNode object
            adding_item._height = 0
            self._header = adding_item
        else:
            if parent_node is None:
                self.add_node(data, self._header, self._header)
            else:
                iter_node = current_node
                if iter_node is None:
                    if isinstance(data, AvlTreeNode):  # check if data is AVLTreeNode
                        adding_item = data
                    else:
                        adding_item = AvlTreeNode(data)  # check if data is AVLTreeNode object
                    adding_item.parent = parent_node
                    adding_item._height = 0
                    if data > parent_node.val:
                        parent_node.right = adding_item
                    else:
                        parent_node.left = adding_item
                elif data > iter_node.val:
                    self.add_node(data, iter_node, iter_node.right)
                    if (self.height(iter_node.right) - self.height(iter_node.left)) == 2:
                        if data > iter_node.right.val:
                            iter_node = self.SingleRotateWithRight(k1=iter_node, k2=iter_node.right)
                        else:
                            iter_node = self.DoubleRotateWithRight(k1=iter_node, k2=iter_node.right.left,
                                                                   k3=iter_node.right)
                    iter_node._height = max(self.height(iter_node.left), self.height(iter_node.right)) + 1
                elif data < iter_node.val:
                    self.add_node(data, iter_node, iter_node.left)
                    if (self.height(iter_node.left) - self.height(iter_node.right)) == 2:
                        if data < iter_node.left.val:
                            iter_node = self.SingleRotateWithLeft(k1=iter_node.left, k2=iter_node)
                        else:
                            iter_node = self.DoubleRotateWithLeft(k1=iter_node.left, k2=iter_node.left.right,
                                                                  k3=iter_node)
                    iter_node._height = max(self.height(iter_node.left), self.height(iter_node.right)) + 1
                else:
                    print('the data already exist')

    def delete(self, data, current_node=None):
        if self._is_empty():
            print('The tree is empty! ')
        else:
            if current_node is None:
                iter_node = self._header
            else:
                iter_node = current_node  # initialize the iter node
            if iter_node.val == data:
                if iter_node.left is None and iter_node.right is None:
                    print('Delete item %d success!' % iter_node.val)
                    iter_node.parent.left = None
                    iter_node.parent.right = None
                elif iter_node.left is not None and iter_node.right is not None:
                    exchange_node = self.findmin(current_node=iter_node.right)
                    print(exchange_node)
                    iter_node.val = exchange_node.val
                    if exchange_node.right is None:
                        exchange_node = None
                    else:
                        exchange_node.parent.left = exchange_node.right
                        exchange_node.right.parent = exchange_node.parent
                        exchange_node.parent.right = None
                    print('Delete item success!')
                else:
                    if iter_node.left:
                        iter_node.parent.left = iter_node.left
                        iter_node.left.parent = iter_node.parent
                    else:
                        iter_node.parent.right = iter_node.right
                        iter_node.right.parent = iter_node.parent
                    print('Delete item success!')
            elif iter_node.val > data:
                self.delete(data, iter_node.left)
            else:
                self.delete(data, iter_node.right)


if __name__ == '__main__':
    import json

    with open("randomlist", "r", encoding='utf-8') as f:
        randomlist = json.loads(f.read())
    myavltree = AvlTree()
    for i in randomlist:
        myavltree.add_node(i)
        # print(i)
        # myavltree.print_all()
    print(randomlist)
    # myavltree.print_path(587)
    # myavltree.print_path(461)
    myavltree.print_all()
