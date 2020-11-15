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
    def Convert(self,pRootOfTree):
        result = self.subConvert(pRootOfTree)
        if isinstance(result,tuple):
            return self.subConvert(pRootOfTree)[0]
        else:
            return result

    def subConvert(self, pRootOfTree):
        if pRootOfTree:
            result = self.subConvert(pRootOfTree.left)
            if isinstance(result,TreeNode):
                left_result = result
                pRootOfTree.left = left_result
                left_result.right = pRootOfTree
            elif result:
                left_result = result[1]
                pRootOfTree.left = left_result
                left_result.right = pRootOfTree
            else:
                left_result = result
            result = self.subConvert(pRootOfTree.right)
            if isinstance(result,TreeNode):
                right_result = result
                pRootOfTree.right = right_result
                right_result.left = pRootOfTree
            elif result:
                right_result = result[0]
                pRootOfTree.right = right_result
                right_result.left = pRootOfTree
            else:
                right_result = result
            if left_result == None and right_result == None:
                return pRootOfTree
            elif right_result == None:
                iter_node = left_result
                while iter_node:
                    left_result = iter_node
                    iter_node = iter_node.left
                return left_result,pRootOfTree
            elif left_result == None:
                iter_node = right_result
                while iter_node:
                    right_result = iter_node
                    iter_node = iter_node.right
                return pRootOfTree,right_result
            else:
                iter_node = right_result
                while iter_node:
                    right_result = iter_node
                    iter_node = iter_node.right
                iter_node = left_result
                while iter_node:
                    left_result = iter_node
                    iter_node = iter_node.left
                return left_result,right_result
        else:
            return None

if __name__ == '__main__':
    import random
    randomlist = [random.randint(0, 999) for i in range(10)]
    #randomlist = [713,27,201,29,516,371,357,404,407,437]
    randomlist = [5]
    #randomlist = [4,6,12,8,16,14,10]
    mysearchtree = SearchTree()
    for i in randomlist:
        mysearchtree.add_node(i)
    mysearchtree.print_all()
    ytree = Solution()
    iter_node = ytree.subConvert(mysearchtree._header)[0]
    #print(iter_node.val)
    while iter_node:
        print(iter_node.val)
        iter_node = iter_node.right
