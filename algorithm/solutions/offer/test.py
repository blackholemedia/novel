#-*- coding=utf-8 -*-
from functools import reduce
import sys
if sys.platform == 'linux':
    sys.path.append('/home/alta/ds')
    from mytree.binarytree import BinaryTree,TreeNode
else:
    sys.path.append('c:\\users\\alta')
    from datastructure.mytree.binarytree import BinaryTree

if __name__ == '__main__':
    b = BinaryTree()
    if b:
        print(1)
    else:
        print(2)
