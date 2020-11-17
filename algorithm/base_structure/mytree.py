# -*- coding=utf-8 -*-
from functools import reduce
import sys
from algorithm.base_structure.listnode import ListNode, Node
from algorithm.base_structure.stack import CreateStack


class TreeNode(Node):

    def __init__(self, item=None, child=None, parent=None, pos_item=None):
        super().__init__(item, pos_item)
        self._child = child
        self._parent = parent


class CreateTree(ListNode):

    def __init__(self):
        super().__init__()

    def returnroot(self):
        if self._is_empty():
            return None
        else:
            return self._header._item

    def add_node(self, data, parentname=None):
        if isinstance(data, TreeNode):
            adding_item = data
        else:
            adding_item = TreeNode(data)  # check if data is TreeNode object
        if self._header is None:
            self._header = adding_item
        else:
            if parentname is None:
                if self._header._child is None:
                    adding_item._parent = self._header
                    self._header._child = adding_item
                else:
                    iter_node = self._header._child
                    while iter_node._pos_item:
                        iter_node = iter_node._pos_item
                    adding_item._parent = iter_node
                    iter_node._pos_item = adding_item
            else:
                parentnode = self.findnode(parentname)
                if isinstance(parentnode, str):
                    print('Input parentname is WRONG, please check it!')
                else:
                    iter_node = parentnode
                    if iter_node._child is None:
                        adding_item._parent = iter_node
                        iter_node._child = adding_item
                    else:
                        iter_node = iter_node._child
                        while iter_node._pos_item:
                            iter_node = iter_node._pos_item
                        adding_item._parent = iter_node
                        iter_node._pos_item = adding_item

    def findnode(self, data):
        if self._is_empty():
            print('The tree is empty. No element found!')
        else:
            iter_node = self._header
            temp_stack = CreateStack()
            while temp_stack._is_empty() == False or iter_node._pos_item is not None or iter_node._child is not None:
                while iter_node:
                    if iter_node._item == data:
                        return iter_node
                    else:
                        if iter_node._child is None:
                            iter_node = iter_node._pos_item
                        else:
                            temp_stack.push(iter_node)
                            iter_node = iter_node._child
                iter_node = temp_stack.returntop()
                iter_node = iter_node._pos_item
                temp_stack.pop()
            if iter_node._item == data:
                return iter_node
            else:
                print('No element found in this tree')

    def print_all(self, depth=0, current_node=None):
        list_depth = depth
        if list_depth == 0:
            iter_node = self._header
        else:
            iter_node = current_node
        if self._is_empty():
            print('The tree is empty!')
        else:
            if iter_node._child is not None:
                if list_depth == 0:
                    print(iter_node._item)
                else:
                    print(reduce(lambda x, y: x + y, ('\t' for i in range(list_depth))), iter_node._item)
                self.print_all(list_depth + 1, iter_node._child)
                if iter_node._pos_item is not None:
                    iter_node = iter_node._pos_item
                    self.print_all(list_depth, iter_node)
            else:
                if list_depth == 0:
                    print(iter_node._item)
                else:
                    print(reduce(lambda x, y: x + y, ('\t' for i in range(list_depth))), iter_node._item)
                iter_node = iter_node._pos_item
                if iter_node is not None:
                    self.print_all(list_depth, iter_node)

    def makeempty(self):
        self._header = None

    def __repr__(self):
        if self._header is None:
            # return 'The tree is empty!'
            return None
        else:
            return self._header


if __name__ == '__main__':
    mytree = CreateTree()
    for i in range(1, 20, 3):
        mytree.add_node(i)
    mytree.add_node(666, 13)
    mytree.add_node(777, 13)
    mytree.add_node(8888, 666)
    mytree.add_node(999, 16)
    mytree.add_node(111, 19)
    mytree.add_node(9999, 666)
    mytree.print_all()
    mytree.makeempty()
    mytree.print_all()
