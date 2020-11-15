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

    def Convert(self, root):
        if root:
            result = self.Convert(root.left)
            if isinstance(result,TreeNode):
                left_result = result
                root.left = left_result
                left_result.right = root
            elif result:
                left_result = result[1]
                root.left = left_result
                left_result.right = root
            else:
                left_result = result
            result = self.Convert(root.right)
            if isinstance(result,TreeNode):
                right_result = result
                root.right = right_result
                right_result.left = root
            elif result:
                right_result = result[0]
                root.right = right_result
                right_result.left = root
            else:
                right_result = result
            if left_result == None and right_result == None:
                return root
            elif right_result == None:
                iter_node = left_result
                while iter_node:
                    left_result = iter_node
                    iter_node = iter_node.left
                return left_result,root
            elif left_result == None:
                iter_node = right_result
                while iter_node:
                    right_result = iter_node
                    iter_node = iter_node.right
                return root,right_result
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
    #randomlist = [7,4,6,5]
    #randomlist = [4,6,12,8,16,14,10]
    mysearchtree = SearchTree()
    for i in randomlist:
        mysearchtree.add_node(i)
    mysearchtree.print_all()
    ytree = Solution()
    iter_node = ytree.Convert(mysearchtree._header)[0]
    #print(iter_node.val)
    while iter_node:
        print(iter_node.val)
        iter_node = iter_node.right
