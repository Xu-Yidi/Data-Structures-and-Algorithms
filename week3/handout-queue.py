# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:45:41 2019

@author: Yidi
"""
'''
Queue
(1)items can only be added to one end and removed from the other, known as the first-in, first-out(FIFO)principle
(2)new items are inserted into a queue at the rear while existing items are removed from the front
(3)basic operations:
a.isEmpty(): return a boolean value indicating whether the queue is empty
b.getSize(): returns the number of items currently in the queue
c.enqueue(item): adds the given item to the back of the queue
d.dequeue(): removes and returns the front item from the queue, an item can not be dequeued from an empty queue
e.getFront(): return a reference to the element at the front of queue without removing it, and an error occurs if the queue is empty
f.getRear(): return a reference to the element at the back of queue without removing it
'''

'''
'''
#%%
#Implementation of the Queue ADT using a Python list
class queue:
    #create an empty queue
    def __init__(self):
        self._qList = list()
    #return true if the queue is empty
    def isEmpty(self):
        return len(self) == 0
    #returns the number of items in the queue
    def __len__(self):
        return len(self._qList)
    #adds the given item to the queue
    def enqueue(self, item):
        self._qList.append(item)
    #removes and returns the first item in the queue
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        return self._qList.pop(0)
    def getFront(self):
        assert not self.isEmpty(), "Cannot getfront from an empty queue"
        return self._qList[0]  
    def getRear(self):
        assert not self.isEmpty(), "Cannot getfront from an empty queue"
        return self._qList[-1]  
#%%
'''
Using a Circular Array
(1)a circular array is simply an array viewed as a circle instead of a line
(2)allows to add new items to a queue and remove existing ones without having to shift items in the process
(3)introduces the concept of a maximum-capacity queue that can become full
(4)uesd with application that require small-capacity and allows for the specification of a maximum size
(5)must maintain a count field and two markers:
a.count field: to keep track of how many items are currently in the queue
b.front and rear: to indicate the array elements containing the first and last items in the queue
'''
#%%
#Implementation of the Queue ADT using a circular array
class Queue:
    
    def __init__(self, maxSize):
        self.count = 0
        self.front = 0
        self.rear = maxSize - 1
        self.qArray = [None] * maxSize
        
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == len(self.qArray)
    
    def getSize(self):
        return self.count
    
    def enqueue(self, item):
        assert not self.isFull(), "Cannot enqueue to a full queue"
        self.rear = (self.rear + 1) % len(self.qArray)
        self.qArray[self.rear] = item
        self.count += 1
    
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        item = self.qArray[self.front]
        self.qArray[self.front] = None
        self.front = (self.front + 1) % len(self.qArray)
        self.count -= 1
        return item

    def getFront(self):
       assert not self.isEmpty(), "Cannot get the first element from an empty queue" 
       return self.qArray[self.front]
    
    def getRear(self):
        assert not self.isEmpty(), "Cannot get the last element from an empty queue"
        return self.qArray[self.rear]
#%%    
#Impementation of the Queue ADT using a linked list
class QueueNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
    
    def isEmpty(self):
        return self.count == 0
    
    def getSize(self):
        return self.count
    
    def enqueue(self, item):
        node = QueueNode(item)
        if self.isEmpty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node
        self.count += 1
        
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        node = self.front
        if self.front is self.rear:
            self.rear = None
        self.front = self.front.next
        self.count -= 1
        return node.item
    
    def getFront(self):
        assert not self.isEmpty(), "Cannot get the first element from an empty queue" 
        return self.front.item
    
    def getRear(self):
        assert not self.isEmpty(), "Cannot get the last element from an empty queue"
        return self.rear.item  
    
        

