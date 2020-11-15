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

    def VerifySquenceOfBST(self, sequence):
        if sequence:
            if len(sequence) < 3:
                return True
            elif len(sequence) == 3:
                if sequence[-1] < sequence[0] and sequence[-1] > sequence[-2]:
                    return False
                else:
                    return True
            elif sequence[-1] > sequence[-2]:
                return self.VerifySquenceOfBST(sequence[:-1])
            elif sequence[-1] < sequence[0]:
                return self.VerifySquenceOfBST(sequence[:-1])
            elif sequence[-1] > sequence[0] and sequence[-1] < sequence[-2]:
                root_index = self.location(sequence[:-1],sequence[-1])
                if reduce(lambda x,y:(x and sequence[-1] > y) if isinstance(x,bool) else (sequence[-1] > x and sequence[-1] > y),sequence[:root_index]) and reduce(lambda x,y:(x and sequence[-1] < y) if isinstance(x,bool) else (sequence[-1] < x and sequence[-1] < y),sequence[root_index:-1]):
                    return self.VerifySquenceOfBST(sequence[:root_index]) and self.VerifySquenceOfBST(sequence[root_index:-1])
                else:
                    return False
            else:
                return False
        else:
            return False

    def location(self, mylist=[], root=None):
        if root > mylist[-1]:
            return len(mylist)
        if len(mylist)%2:
            half_length = len(mylist)//2 + 1
        else:
            half_length = len(mylist)//2
        if root < mylist[half_length]:
            return self.location(mylist[:half_length],root)
        else:
            return half_length + self.location(mylist[half_length:],root)


if __name__ == '__main__':
    import random
    #randomlist = [random.randint(0, 999) for i in range(20)]
    #randomlist = [5,4,3,2,1]
    #randomlist = [7,4,6,5]
    randomlist = [4,6,12,8,16,14,10]
    '''
    mybinarytree = BinaryTree()
    for i in randomlist:
        mybinarytree.add_node(i)
    mybinarytree.print_all()
    '''
    ytree = Solution()
    print(ytree.VerifySquenceOfBST(randomlist))
