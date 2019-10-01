# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:13:18 2019

@author: Yidi
"""

'''
Stacks
(1) inserted and removed sccording to the last-in, first-out(LIFO) principle
(2) top of the stack/ base of the stack
(3) basic operations:
a. isEmpty(): returna boolean value indicating if the stack is empty
b. getSize(): returns the number of items in the stack
c. pop(): remove and returns the top item of the stack, if the stack is not empty, 
          and the next item on the stack becomes the new top item
d. push(item): adds the given item to the top of the stack
e. peek(): returns a reference to the item on top of a non-empty stack without removing it
(4) the stack ADT can be implemented by the use of Python list and a linked list
'''
#implementaion of the stack ADT using a Python list
class Stack:
    #creates an empty stack()
    def __init__(self):
        self.items = list()
    #return True if the stack is empty
    def isEmpty(self):
        return len(self.items) == 0
    #return the number of items in the stack
    def getSize(self):
        return len(self.items)
    #return the top item on the stack without removing it
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self.items[-1]
    #remove and returns the top item on the stack
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self.items.pop()
    #push an item onto the top of thr stack
    def push(self, item):
        self.items.append(item)
        
#implementaion of the stack ADT using a singly linked list
class StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link

class Stack:
    #create an empty stack
    def __init__(self):
        self.top = None
        self.size = 0
    #return True if the stack is empty 
    def isEmpty(self):
        return self.top is None
    #return the number of items in the stack
    def getSize(self):
        return self.size
    #return the top item on the stack without removing it
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self.top.item
    #remove and returns the top item on the stack
    def pop(self):
        assert not self.isEmpty(), "Cannot pop at an empty stack"
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node.item
    #pushes an item onto the top of the stack
    def push(self, item):
        self.top = StackNode(item, self.top)
        self.size += 1
        








