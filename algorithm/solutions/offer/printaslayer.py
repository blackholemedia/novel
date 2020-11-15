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

    def PrintAsLayer(self, root):
        # write code here
        if root:
            self.result.append([root.val])
            top = self.circular(root)
            if top:
                if isinstance(top,TreeNode):
                    iter_list = [top]
                else:
                    iter_list = [x for x in top]
                while iter_list:
                    plist = []
                    printlist = []
                    for iter_node in iter_list:
                        printlist.append(iter_node.val)
                        i = self.circular(iter_node)
                        if isinstance(i,tuple):
                            plist.append(i[0])
                            plist.append(i[1])
                        elif i:
                            plist.append(i)
                        else:
                            pass
                    iter_list = plist
                    self.result.append(printlist)
                return self.result
            else:
                return self.result
        else:
            return self.result

    def circular(self, root):
        if root == None:
            return None
        else:
            # self.result.append(root.val)
            if root.left and root.right:
                return (root.left,root.right)
            elif root.left != None:
                return root.left
            elif root.right != None:
                return root.right
            else:
                return None

if __name__ == '__main__':
    import random
    #randomlist = [random.randint(0, 999) for i in range(20)]
    randomlist = [5]
    mybinarytree = BinaryTreeFromList()
    for i in randomlist:
        mybinarytree.add_node(i)
    mybinarytree.print_all()
    mybinarytree.dec_alergic()
    mybinarytree.print_all()
    ytree = Solution()
    print(ytree.PrintAsLayer(mybinarytree._header))
