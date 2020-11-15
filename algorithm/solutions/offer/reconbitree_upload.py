#-*- coding=utf-8 -*-
from functools import reduce
import sys
if sys.platform == 'linux':
    sys.path.append('/home/alta/ds')
    from mytree.binarytree import BinaryTree,TreeNode
else:
    sys.path.append('c:\\users\\alta')
    from datastructure.mytree.binarytree import BinaryTree,TreeNode


class Solution(BinaryTree):
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        root_index = tin.index(pre[0])
        if len(pre) == 1:
            return TreeNode(pre[0])
        elif len(pre) == 2:
            next_node = TreeNode(pre[1])
            root_node = TreeNode(pre[0])
            if tin.index(pre[1]) < tin.index(pre[0]):
                root_node.left = next_node
            else:
                root_node.right = next_node
            return root_node
        else:
            root_node = TreeNode(pre[0])
            root_node.left =  self.reConstructBinaryTree(pre[1:root_index+1], tin[:root_index])
            root_node.right = self.reConstructBinaryTree(pre[root_index+1:],tin[root_index+1:])
            return root_node

if __name__ == '__main__':
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    mybinarytree = Solution()
    mybinarytree._header = mybinarytree.reConstructBinaryTree(pre, tin)
    mybinarytree.print_all()
