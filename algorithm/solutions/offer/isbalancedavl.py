#-*- coding=utf-8 -*-
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

    def IsBalanced_Solution(self, pRoot):
        if isinstance(self.get_height(pRoot),bool):
            return False
        else:
            return True

    def get_height(self, pRoot):
        if pRoot:
            left_result = self.get_height(pRoot.left)
            right_result = self.get_height(pRoot.right)
            if isinstance(left_result,bool) or isinstance(right_result,bool):
                return False
            elif abs(left_result - right_result) > 1:
                return False
            else:
                return max(left_result,right_result) + 1
        else:
            return -1

if __name__ == '__main__':
    import random
    randomlist = [random.randint(0, 999) for i in range(10)]
    #randomlist = [713,27,201,29,516,371,357,404,407,437]
    #randomlist = [4,6,12,8,16,14,10]
