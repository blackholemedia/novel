# -*- coding=utf-8 -*-
from functools import reduce
import sys, random

if sys.platform == 'linux':
    sys.path.append('/home/alta/ds')
    from mytree.tree import CreateTree
else:
    sys.path.append('c:\\users\\alta')
    from datastructure.mytree.tree import CreateTree


class TreeNode(object):

    def __init__(self, data=None):
        self.val = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.val)


class BinaryTree(CreateTree):

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
                if random.randint(0, 999) % 2 == 0:
                    self.add_node(data, iter_node.left)
                else:
                    self.add_node(data, iter_node.right)

    def findnode(self, data, current_node=None):
        if self._is_empty():
            print('The tree is empty. No element found!')
        else:
            if current_node is None:
                iter_node = self._header
            else:
                iter_node = current_node
            if data == iter_node.val:
                return iter_node
            elif data > iter_node.val:
                if iter_node.right:
                    return self.findnode(data, iter_node.right)
                else:
                    return 'No element found in this tree'
            else:
                if iter_node.left:
                    return self.findnode(data, iter_node.left)
                else:
                    return 'No element found in this tree'

    def findmin(self, current_node=None):
        if self._is_empty():
            print('The tree is empty. No element found!')
        else:
            if current_node is None:
                iter_node = self._header
            else:
                iter_node = current_node
            if iter_node.left:
                return self.findmin(iter_node.left)
            else:
                return iter_node

    def findmax(self, current_node=None):
        if self._is_empty():
            print('The tree is empty. No element found!')
        else:
            if current_node is None:
                iter_node = self._header
            else:
                iter_node = current_node
            if iter_node.right:
                return self.findmax(iter_node.right)
            else:
                return iter_node

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
                elif iter_node.left != None and iter_node.right != None:
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

    def print_path(self, data, current_node=None):
        if self._is_empty():
            print('The tree is empty! ')
        else:
            if current_node is None:
                iter_node = self._header
            else:
                iter_node = current_node
            if data == iter_node.val:
                print(iter_node.val)
                # iter_node
            elif data > iter_node.val:
                print(iter_node.val)
                if iter_node.right:
                    self.print_path(data, iter_node.right)
                else:
                    print('No element %d found in this tree' % data)
            else:
                print(iter_node.val)
                if iter_node.left:
                    self.print_path(data, iter_node.left)
                else:
                    print('No element %d found in this tree' % data)

    def print_all(self, current_node=None, node_depth=0):
        if self._is_empty():
            print('The tree is empty!')
        else:
            if current_node is None:
                iter_node = self._header
            else:
                iter_node = current_node
            if node_depth == 0:
                print(iter_node.val)
            else:
                print(reduce(lambda x, y: x + y, ('\t' for i in range(node_depth))), iter_node.val)
            if iter_node.left and iter_node.right:
                self.print_all(iter_node.right, node_depth + 1)
                self.print_all(iter_node.left, node_depth + 1)
            elif iter_node.left != None:
                self.print_all(iter_node.left, node_depth + 1)
            elif iter_node.right != None:
                self.print_all(iter_node.right, node_depth + 1)
            else:
                return None


if __name__ == '__main__':
    import random, json

    with open("randomlist", "r", encoding='utf-8') as f:
        randomlist = json.loads(f.read())
    mybinarytree = BinaryTree()
    for i in randomlist:
        mybinarytree.add_node(i)
    print(randomlist)
    mybinarytree.print_all()
