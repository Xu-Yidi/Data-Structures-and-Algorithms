# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:03:51 2019

@author: Yidi
"""


'''
Linked List

1.A linked structure contains a collection of objects called nodes, each of which contains data and at least one reference or link to another node
2.A linked list is a structure in which the nodes are connected in sequence to form a linear list
(1)The first node in the list(head node), must be named or referenced by external variable
(2)The last node in the list(tail node), is indicated by a null link reference
(3)A linked list can be empty, which can be indicated when the head reference is null

The Singly Linked List
1.A singly linked list is a linked list in which each node contains a single link field and allows for a complete traversal from a distinctive first node to the last
'''
#%%
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
#class ListNode includes two attributes: the data and the reference next to anonther node
#%%
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    #traversing linked list items
    def traversal(self):
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            curNode = self.head
            while curNode is not None:
                print(curNode.data, " ")
                curNode = curNode.next
    #inserting items
    def insertAtHead(self, data):
        newNode = ListNode(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1
    
    def insertAtTail(self, data):
        newNode = ListNode(data)
        if self.head is None:
            self.head = newNode
        else:
            curNode = self.head
            while curNode.next is not None:
                curNode = curNode.next
            curNode.next = newNode
        self.size += 1
    
    def insertAtIndex(self, index, data):
        if index > self.size:
            return
        elif index <= 0:
            self.insertAtHead(data)
        else:
            newNode = ListNode(data)
            curNode = self.head
            for i in range(0, index-1):
                curNode = curNode.next
            newNode.next = curNode.next
            curNode.next = newNode
            self.size += 1
    #searching for a node
    def search(self, target):
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            curNode = self.head
            while curNode is not None:
                if curNode.data == target:
                    print("Node found")
                    return True
                curNode = curNode.next
            print("Node not found")
            return False
    #deleting elements
    def deleteAtHead(self):
        if self.head is None:
            print("Linked list has no element to delete")
            return
        else:
            curNode = self.head
            self.head = curNode.next
            del curNode
            self.size -= 1
    def deleteAtTail(self):
        if self.head is None:
            print("Linked list has no element to delete")
            return
        else:
            curNode = self.head
            while curNode.next.next is not None:
                curNode = curNode.next
            curNode.next = None            
            self.size -= 1
    def deleteAtIndex(self, index):
        if self.head is None:
            print("Linked list has no element to delete")
            return
        elif index >= self.size:
            return
        elif index == 0:
            self.deleteAtHead()
        else:
            curNode = self.head
            for i in range(0, index - 1):
                curNode = curNode.next
            curNode.next = curNode.next.next
            self.size -= 1
    #reverseing linkes list
    def reverseIterative(self):
        if self.head is None:
            return
        else:
            preNode = None
            curNode = self.head
            while curNode is not None:
                next = curNode.next
                curNode.next = preNode
                preNode = curNode
                curNode = next
            self.head = preNode 
#%%      
#testing          
new_linked_list = LinkedList()        
new_linked_list.insertAtHead(5)
new_linked_list.insertAtHead(10)
new_linked_list.insertAtHead(15)       
new_linked_list.reversal()
new_linked_list.traversal()

        












