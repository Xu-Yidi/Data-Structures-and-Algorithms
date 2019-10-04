# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 01:14:09 2019
@author: Yidi
"""

class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:
 
    def __init__(self):
        self.head = None
        self.size = 0
 
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1        
        cur = self.head        
        for i in range(0, index):            
            cur = cur.next 
        return cur.val
    
    def addAtHead(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
 
    def addAtTail(self, val):
        cur = self.head
        if cur == None:
            self.head = Node(val)
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = Node(val)
        self.size += 1
        
 
    def addAtIndex(self, index, val):
        if index > self.size:
            return   
        if index <= 0:
            self.addAtHead(val)
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            node = Node(val)     
            node.next = cur.next
            cur.next = node
            self.size += 1
        
    def deleteAtIndex(self, index):

        if index < 0 or index >= self.size:
            return
        
        cur = self.head
        
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(0, index - 1):
                cur = cur.next
            cur.next = cur.next.next              
 
        self.size -= 1

    
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
