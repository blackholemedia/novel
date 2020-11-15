#-*- coding=utf-8 -*-
from functools import reduce
import sys
if sys.platform == 'linux':
    sys.path.append('/home/alta/ds')
    from mytree.binarytree import BinaryTree, TreeNode
else:
    sys.path.append('c:\\users\\alta')
    from datastructure.mytree.binarytree import BinaryTree, TreeNode


class Solution(BinaryTree):

    def __init__(self):
        super().__init__()
        self.copytree = None

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

    def generate_copy(self, source_node=None, target_node=None):
        if source_node:
            if self.copytree:
                if source_node.left == None and source_node.right == None:
                    return None
                else:
                    if source_node.left:
                        target_node.left = TreeNode(source_node.left.val)
                        self.generate_copy(source_node.left, target_node.left)
                    else:
                        pass
                    if source_node.right:
                        target_node.right = TreeNode(source_node.right.val)
                        self.generate_copy(source_node.right, target_node.right)
                    else:
                        pass
            else:
                self.copytree = TreeNode(source_node.val)
                iter_node = self.copytree
                if source_node.left == None and source_node.right == None:
                    return None
                else:
                    self.generate_copy(source_node, iter_node)
            return self.copytree
        else:
            return None

    def comp(self,tree1,tree2):
        if tree1:
            if tree2:
                if tree1.val != tree2.val:
                    return False
                else:
                    return self.comp(tree1.left,tree2.left)
                    return self.comp(tree1.right,tree2.right)
            else:
                return False
        else:
            if tree2:
                return False
            else:
                return True

    def isSymmetrical(self,pRoot):
        mirror_tree = self.generate_copy(pRoot)
        self.Mirror(pRoot)
        return self.comp(mirror_tree,pRoot)

if __name__ == '__main__':
    import random
    randomlist = [random.randint(0, 999) for i in range(20)]
    #randomlist = [8,6,6,5,7,7,5]
    mybinarytree = BinaryTree()
    for i in randomlist:
        mybinarytree.add_node(i)
    mybinarytree.print_all()
    ytree = Solution()
    print(ytree.isSymmetrical(mybinarytree))
