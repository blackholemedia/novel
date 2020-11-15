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
        self.result = []

    def PrintFromTopToBottom(self, pRoot):
        # write code here
        if pRoot:
            self.result.append(pRoot.val)
            top = self.circular(pRoot)
            if isinstance(top,TreeNode):
                iter_list = [top]
            elif top:
                iter_list = [x for x in top]
            else:
                return self.result
            while iter_list:
                plist = []
                for iter_node in iter_list:
                    self.result.append(iter_node.val)
                    i = self.circular(iter_node)
                    if isinstance(i,tuple):
                        plist.append(i[0])
                        plist.append(i[1])
                    elif i:
                        plist.append(i)
                    else:
                        pass
                iter_list = plist
            return self.result
        else:
            return self.result

    def circular(self, pRoot):
        if pRoot == None:
            return None
        else:
            if pRoot.left and pRoot.right:
                return (pRoot.left,pRoot.right)
            elif pRoot.left != None:
                return pRoot.left
            elif pRoot.right != None:
                return pRoot.right
            else:
                return None

if __name__ == '__main__':
    import random
    #randomlist = [random.randint(0, 999) for i in range(20)]
    randomlist = [5,4,'#',3,'#',2,'#',1]
    mybinarytree = BinaryTreeFromList()
    for i in randomlist:
        mybinarytree.add_node(i)
    mybinarytree.print_all()
    mybinarytree.dec_alergic()
    mybinarytree.print_all()
    ytree = Solution()
    print(ytree.PrintFromTopToBottom(mybinarytree._header))
