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
        self.add_result = 0
        self.mylist = []
        self.result = []

    def FindPath(self, root, expectNumber):
        if root:
            if self.add_result + root.val == expectNumber:
                if root.left == None and root.right == None:
                    self.mylist.append(root.val)
                    self.result.append([x for x in self.mylist])
                    self.mylist.pop()
                else:
                    return None
            elif self.add_result + root.val > expectNumber:
                return None
            else:
                self.add_result += root.val
                self.mylist.append(root.val)
                self.FindPath(root.left, expectNumber)
                self.FindPath(root.right, expectNumber)
                if root:
                    self.add_result -= root.val
                    self.mylist.pop()
        else:
            return None

if __name__ == '__main__':
    import random
    #randomlist = [random.randint(0, 999) for i in range(20)]
    randomlist = [10,5,12,4,7]
    mybinarytree = BinaryTreeFromList()
    for i in randomlist:
        mybinarytree.add_node_byleft(i)
    mybinarytree.print_all()
    #mybinarytree.dec_alergic()
    #mybinarytree.print_all()
    ytree = Solution()
    ytree.FindPath(mybinarytree._header, 15)
    print(ytree.result)
