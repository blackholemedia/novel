# -*- coding=utf-8 -*-


class Node(object):

    def __init__(self, item=None, pos_item=None):
        self._item = item
        self._pos_item = pos_item

    def __repr__(self):
        return str(self._item)


class ListNode(object):

    def __init__(self):
        self._header = None
        self._pos_item = None
        self.__length = 0

    def __repr__(self):
        return self._header

    def _is_empty(self):
        return self._header is None

    def add_node(self, nextnode):
        if isinstance(nextnode, Node):
            adding_item = nextnode
        else:
            adding_item = Node(nextnode)  # check if nextnode is Node object

        if self._header is None:
            self._header = adding_item
            self.__length += 1
        else:
            iter_node = self._header
            while iter_node._pos_item:
                iter_node = iter_node._pos_item
            iter_node._pos_item = adding_item
            self.__length += 1

    def del_node(self, index):
        iter_node = self._header
        iter_index = 1
        if 1 == index:
            self._header = self._header._pos_item
            self.__length -= 1
        elif index > self.__length:
            print('Index out of range')
        else:
            while iter_index < index - 1:
                iter_node = iter_node._pos_item
                iter_index += 1
            iter_node._pos_item = iter_node._pos_item._pos_item
            self.__length -= 1

    def insert_node(self, index, data):
        if index < 1 or index > self.__length + 1:
            print('Index out of range')
        elif index == 1:
            node = Node(data)
            node._pos_item = self._header
            self._header = node
            self.__length += 1
        else:
            iter_node = self._header
            node = Node(data)
            iter_index = 1
            while iter_index < index - 1:
                iter_node = iter_node._pos_item
                iter_index += 1
            node._pos_item = iter_node._pos_item
            iter_node._pos_item = node
            self.__length += 1

    def update(self, index, data):
        if index < 0 or index > self.__length:
            print('Index out of range')
        else:
            iter_node = self._header
            iter_index = 1
            while iter_index < index:
                iter_node = iter_node._pos_item
                iter_index += 1
            iter_node._item = data

    def get_item(self, index):
        if index < 0 or index > self.__length:
            print('Index out of range')
        else:
            iter_node = self._header
            iter_index = 1
            while iter_index < index:
                iter_node = iter_node._pos_item
                iter_index += 1
            return iter_node._item

    def get_index(self, data):
        iter_node = self._header
        iter_index = 1
        while iter_node:
            if iter_node._item == data:
                return iter_index
            else:
                iter_node = iter_node._pos_item
                iter_index += 1
        print("%s not found" % data)
        return

    def clear(self):
        self._header = Node
        self.__length = 0

    def __repr__(self):
        if self._is_empty():
            return 'The listtable is empty'
        else:
            iter_node = self._header
            nlist = ''
            while iter_node._pos_item is not None:
                nlist += str(iter_node._item)
                iter_node = iter_node._pos_item
            nlist += str(iter_node._item)
        return nlist


if __name__ == '__main__':
    '''
    mylist = ListNode()
    for i in range(0,20,2):
        mylist.add_node(i)
    mylist.del_node(5)
    mylist.insert_node(10,17)
    mylist.update(5,33)
    print(mylist,mylist.__length)
    print(mylist.get_index(7))
    '''
    i = Node(2, 7)
    print(i)
