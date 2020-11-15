#-*- coding=utf-8 -*-
from functools import reduce
import sys
if sys.platform == 'linux':
    sys.path.append('/home/alta/ds')
    from mytree.binarytree import BinaryTree
    from mytree.tree import TreeNode
else:
    sys.path.append('c:\\users\\alta')
    from datastructure.mytree.binarytree import BinaryTree
    from datastructure.mytree.tree import TreeNode


class Solution(BinaryTree):

    def Mirror(self, root):
        if root:
            if root.left == None and root.right == None:
                return None
            elif root.left == None:
                root.left = root.right
                root.right = None
                self.Mirror(root.left)
            elif root.right == None:
                root.right = root.left
                root.left = None
                self.Mirror(root.right)
            else:
                p = root.left
                root.left = root.right
                root.right = p
                self.Mirror(root.left)
                self.Mirror(root.right)
            return root
        else:
            return None

if __name__ == '__main__':
    import random
    randomlist = [random.randint(0, 999) for i in range(20)]
    mybinarytree = BinaryTree()
    for i in randomlist:
        mybinarytree.add_node(i)
    mybinarytree.print_all()
    ytree = Solution()
    ytree.Mirror(mybinarytree._header)
    mybinarytree.print_all()
