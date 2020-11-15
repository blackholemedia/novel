#-*- coding=utf-8 -*-
from linkedlist.stack import CreateStack
from linkedlist import listnode

def toposfix():
    SYMBOL_SERIES = ['+','-','*','\\','(','[','{','<',')',']','}','>']
    check_stack = CreateStack()
    check_stack.push('*')
    print(check_stack.returntop())
    print(SYMBOL_SERIES.index(check_stack.returntop()))

if __name__ == '__main__':
    p1 = 'a + b * c + (d * e + f) * g'
    toposfix()
