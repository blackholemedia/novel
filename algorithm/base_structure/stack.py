#-*- coding=utf-8 -*-

import sys
if sys.platform == 'linux':
    sys.path.append('/home/alta/ds')
    from mylinkedlist.listnode import ListNode,Node
else:
    sys.path.append('c:\\users\\alta')
    from datastructure.mylinkedlist.listnode import ListNode,Node

class CreateStack(ListNode):

    def __init__(self):
        super().__init__()

    def returntop(self):
        if self._is_empty():
            return None
        else:
            return self._header._item

    def push(self,data):
        self.insert_node(1,data)

    def pop(self):
        if self._is_empty():
            print('The Stack is empty. No element to pop!')
        else:
            self.del_node(1)

    def __repr__(self):
        if self._header == None:
            return 'The stack is empty!'
        else:
            return self._header

if __name__ == '__main__':
    mystack = CreateStack()
    print(mystack)
    print(mystack.returntop())
    mystack.push(12)
    print(mystack.returntop())
    mystack.pop()
    print(mystack.returntop())
