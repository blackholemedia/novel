#-*- coding=utf-8 -*-
from functools import reduce
import sys
if sys.platform == 'linux':
    sys.path.append('/home/alta/ds')
    from mytree.binarytreefromlist import BinaryTreeFromList
    from mytree.tree import TreeNode
else:
    sys.path.append('c:\\users\\alta')
    from datastructure.mytree.binarytreefromlist import BinaryTreeFromList
    from datastructure.mytree.tree import TreeNode


class Solution(BinaryTreeFromList):

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                if pRoot2.left and pRoot2.right:
                    if self.HasSubtree(pRoot1.left,pRoot2.left) and self.HasSubtree(pRoot1.right,pRoot2.right):
                        return True
                    else:
                        return self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
                elif pRoot2.left:
                    if self.HasSubtree(pRoot1.left,pRoot2.left):
                        return True
                    else:
                        return self.HasSubtree(pRoot1.left,pRoot2)
                elif pRoot2.right:
                    if self.HasSubtree(pRoot1.right,pRoot2.right):
                        return True
                    else:
                        return self.HasSubtree(pRoot1.right,pRoot2)
                else:
                    return True
            else:
                return False
        else:
            return False

    def getsubtree(self, parent_tree=None):
        iter_node = parent_tree
        for i in range(4):
            if i % 2 == 0:
                iter_node = parent_tree.left
            else:
                iter_node = iter_node.right
        return iter_node

if __name__ == '__main__':
    import random
    #randomlist = [random.randint(0, 999) for i in range(20)]
    mybinarytree = BinaryTreeFromList()
    #for i in [8,8,7,9,2,'#','#','#','#',4,7]:
    for i in [8,'#',9,3,2]:
        mybinarytree.add_node_byleft(i)
    mybinarytree.dec_alergic()
    mybinarytree.print_all()
    #otherlist = [random.randint(0, 999) for i in range(5)]
    othertree = BinaryTreeFromList()
    #for i in [8,9,2]:
    #    othertree.add_node_byleft(i)
    othertree.print_all()
    ytree = Solution()
    #subtree = ytree.getsubtree(mybinarytree._header)
    #print(subtree)
    #print(ytree.HasSubtree(mybinarytree._header, subtree))
    print(ytree.HasSubtree(mybinarytree._header, othertree._header))
