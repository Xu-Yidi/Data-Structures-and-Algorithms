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
            return
        else:
            curNode = self.find_last_node(index)[0]
            curNode.next = ListNode(hash_value)
            return

    def remove(self, key):
        hash_value = self.hash_function(key)
        index = self.add_index(key)
        
        if self.data[index] is None:
            return
        
        index_value = self.find_last_node(index)[1]
        times = index_value.count(hash_value)
        
        for i in range(times):
            preNode = self.data[index]
            if self.data[index].val == hash_value:
                self.data[index] = preNode.next
            else:
                curNode = self.data[index].next
                while curNode is not None:
                    if curNode.val ==  hash_value:
                        preNode.next = curNode.next
                        curNode = curNode.next
                        break
                    else:
                        preNode, curNode = preNode.next, curNode.next   
           
    def contains(self, key):
        hash_value = self.hash_function(key)
        index = self.add_index(key)
        
        if self.data[index] is None:
            return False
        else:
            index_value = self.find_last_node(index)[1]
            if hash_value in index_value:
                return True
            else:
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
        
    def find_last_node(self, index):
        if self.data[index] is None:
            return
        else:            
            index_value = []
            curNode = self.data[index]
            while curNode.next is not None:
                index_value.append(curNode.val)
                curNode = curNode.next
            index_value.append(curNode.val)
            return [curNode, index_value]

#Reference:
#linked list之概念參考week2自行整理之資料https://github.com/Xu-Yidi/fluteanzi/blob/master/week2/handout-singly%20linked%20list.py
#程式為自行撰寫
