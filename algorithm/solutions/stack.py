# -*- coding=utf-8 -*-


class Stack(object):

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack:
            return False
        else:
            return True

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print('The Stack is empty. No element to pop!')
        else:
            self.stack.pop()

    def __repr__(self):
        if self.is_empty():
            return 'The stack is empty!'
        else:
            return self.stack[0]


if __name__ == '__main__':
    mystack = Stack()
    print(mystack)
    print(mystack.top())
    mystack.push(12)
    print(mystack.top())
    mystack.pop()
    print(mystack.top())
