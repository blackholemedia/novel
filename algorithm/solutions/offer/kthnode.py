# -*- coding=utf-8 -*-
from functools import reduce
import sys

if sys.platform == 'linux':
    sys.path.append('/home/alta/ds')
    from mytree.searchtree import SearchTree
    from mytree.binarytree import TreeNode
else:
    sys.path.append('c:\\users\\alta')
    from datastructure.mytree.searchtree import SearchTree
    from datastructure.mytree.binarytree import TreeNode


class Solution(SearchTree):

    def __init__(self):
        super().__init__()

    def KthNode(self, root, k):
        if root == None:
            return None
        elif k == 1:
            return self.findmin(root)
        elif k == 0:
            return None
        else:
            if root.left != None:
                left_amount = self.count(root.left)
            else:
                left_amount = 0
            if left_amount == k:
                return self.findmax(root.left)
            elif left_amount == k - 1:
                return root
            elif left_amount < k:
                if root.right == None:
                    return None
                else:
                    return self.KthNode(root.right, k - 1 - left_amount)
            else:
                return self.KthNode(root.left, k)

    def count(self, root):
        # write code here
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        elif root.right == None:
            return 1 + self.count(root.left)
        else:
            return self.count(root.left) + 1 + self.count(root.right)

    def findmax(self, current_node=None):
        iter_node = current_node
        if iter_node.right:
            return self.findmax(iter_node.right)
        else:
            return iter_node

    def findmin(self, current_node=None):
        iter_node = current_node
        if iter_node.left:
            return self.findmin(iter_node.left)
        else:
            return iter_node


if __name__ == '__main__':
    import random

    randomlist = [random.randint(0, 999) for i in range(20)]
    print(randomlist)
    mysearchtree = SearchTree()
    for i in randomlist:
        mysearchtree.add_node(i)
    mysearchtree.print_all()
    ytree = Solution()
    print(ytree.KthNode(mysearchtree._header, 22))
