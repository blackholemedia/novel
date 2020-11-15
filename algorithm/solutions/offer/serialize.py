#-*- coding=utf-8 -*-
from functools import reduce
import sys
if sys.platform == 'linux':
    sys.path.append('/home/alta/ds')
    from mytree.binarytree import TreeNode,BinaryTree
else:
    sys.path.append('c:\\users\\alta')
    from datastructure.mytree.binarytree import TreeNode,BinaryTree


class Solution(BinaryTree):

    def __init__(self):
        super().__init__()
        self.datatype = None

    def serialize(self,root):  # middle list
        if self.datatype == None:
            self.datatype = type(root.val)
        if root == None:
            return ''
        elif root.left == None and root.right == None:
            return '#' + str(root.val)
        elif root.left == None:
            return str(root.val) + ' ' + self.serialize(root.right)
        elif root.right == None:
            return self.serialize(root.left) + ' ' + str(root.val)
        else:
            return self.serialize(root.left) + ' ' + '!' + str(root.val) + ' ' + self.serialize(root.right)

    def deserialize(self, string):  # middle list
        string_list = string.split(' ')
        string_length = len(string_list)
        root = None
        pre_flag = ''
        pre_node = None
        left = True
        for i in string_list:
            if pre_flag == '':
                if i[0] == '#':
                    if pre_node:
                        leaf = TreeNode(int(i[1:]))
                        pre_node.right = leaf
                        pre_node = leaf
                        pre_flag = '#'
                    else:  # the first leaf
                        leaf = TreeNode(int(i[1:]))
                        pre_node = leaf
                        pre_flag = '#'
                elif i[0] == '!':
                    binary_node = TreeNode(int(i[1:]))
                    binary_node.left = pre_node
                    pre_flag = '!'
                    pre_node = binary_node
                    #  is it the root node?
                else:
                    single_node = TreeNode(int(i[1:]))
                    single_node.right = pre_node
                    pre_flag = ''
                    pre_node = single_node
                    left = False
            elif pre_flag == '#':
                if i[0] == '#':
                    print('serizalize ERROR')
                elif i[0] == '!':
                    binary_node = TreeNode(int(i[1:]))
                    binary_node.left = pre_node
                    pre_flag = '!'
                    pre_node = binary_node
                else:
                    single_node = TreeNode(int(i[1:]))
                    single_node.left = pre_node
                    pre_flag = ''
                    pre_node = single_node
            else:
                if i[0] == '#':
                    leaf = TreeNode(int(i[1:]))
                    pre_node.right = leaf #  current node is right of pre-node
                    iter_node = pre_node # iter node is pre-node
                    pre_node = leaf
                    pre_flag = '#'
                    if root == iter_node.left:
                        root = iter_node
                elif i[0] == '!':
                    print('serizalize ERROR')
                else:
                    single_node = TreeNode(int(i[1:]))
                    single_node.right = pre_node
                    pre_flag = ''
                    pre_node = single_node

if __name__ == '__main__':
    import random
    randomlist = [random.randint(0, 999) for i in range(20)]
    print(randomlist)
    mytesttree = BinaryTree()
    for i in randomlist:
        mytesttree.add_node(i)
    mytesttree.print_all()
    ytree = Solution()
    serial_result = ytree.serialize(mytesttree._header)
    print(serial_result)
    # destree = ytree.deserialize(serial_result)
