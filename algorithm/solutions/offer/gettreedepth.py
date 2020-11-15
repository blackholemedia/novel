#-*- coding=utf-8 -*-
from functools import reduce
import sys
if sys.platform == 'linux':
    sys.path.append('/home/alta/ds')
    from mytree.binarytreefromlist import BinaryTreeFromList
    from mytree.binarytree import TreeNode
else:
    sys.path.append('c:\\users\\alta')
    from datastructure.mytree.binarytreefromlist import BinaryTreeFromList
    from datastructure.mytree.binarytree import TreeNode


class Solution(BinaryTreeFromList):

    def __init__(self):
        super().__init__()

    def TreeDepth(self, pRoot):
        if pRoot:
            return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
        else:
            return 0

if __name__ == '__main__':
    import random
    randomlist = [random.randint(0, 999) for i in range(20)]
    #randomlist = [5]
    mybinarytree = BinaryTreeFromList()
    for i in randomlist:
        mybinarytree.add_node(i)
    mybinarytree.print_all()
    #mybinarytree.dec_alergic()
    #mybinarytree.print_all()
    ytree = Solution()
    print(ytree.TreeDepth(mybinarytree._header))
