# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:47:17 2019
@author: Yidi
"""

from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        hash_value = self.hash_function(key)
        index = self.add_index(key)
        
        if self.data[index] is None:
            self.data[index] = ListNode(hash_value)
        else:
            curNode = self.data[index]
            while curNode.next is not None:
                curNode = curNode.next
            curNode.next = ListNode(hash_value)

    def remove(self, key):
        hash_value = self.hash_function(key)
        index = self.add_index(key)
                
        while self.contains(key) is True:
            if self.data[index].val == hash_value:
                self.data[index] = self.data[index].next
            else:
                preNode = self.data[index]
                curNode = self.data[index].next
                while curNode is not None:
                    if curNode.val == hash_value:
                        preNode.next = curNode.next
                        curNode = curNode.next
                    else:
                        curNode = curNode.next
                        preNode = preNode.next    
    
    def contains(self, key):
        hash_value = self.hash_function(key)
        index = self.add_index(key)
        
        if self.data[index] is None:
            return False
        else:
            curNode = self.data[index]
            while curNode is not None:
                if curNode.val == hash_value:
                    return True
                else:
                    curNode = curNode.next
            return False
                   
    def hash_function(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))      
        hash_value = h.hexdigest()
        return hash_value                  
       
    def add_index(self, key):
        hash_value = self.hash_function(key)
        index = int(hash_value, 16) % self.capacity
        return index
