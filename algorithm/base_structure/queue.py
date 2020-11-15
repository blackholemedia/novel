#-*- coding=utf-8 -*-

import sys
sys.path.append('/home/alta/ds')
from mylinkedlist.listnode import ListNode,Node
# sys.path.append('c:\\users\\alta')
# from datastructure.mylinkedlist.listnode import ListNode,Node

class CreateQueue(ListNode):

    def __init__(self):
        super().__init__()

    def returnhead(self):
        if self._is_empty():
            return None
        else:
            return self._header._item

    def enqueue(self,data):
        self.insert_node(self._length+1,data)

    def dequeue(self):
        if self._is_empty():
            print('The queue is empty. No element to pop!')
        else:
            self.del_node(1)

    def __repr__(self):
        if self._length == 0:
            return 'The queue is empty!'
        else:
            return self._header

if __name__ == '__main__':
    mystack = CreateQueue()
    print(mystack)
    mystack.enqueue(12)
    mystack.enqueue(7)
    print(mystack.returnhead())
    mystack.dequeue()
    print(mystack.returnhead())
