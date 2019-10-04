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
class Queue:
    #create an empty queue
    def __init__(self):
        self._qList = list()
    #return true if the queue is empty
    def isEmpty(self):
        return len(self) == 0
    #returns the number of items in the queue
    def getSize(self):
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
        self._count = 0
        self._front = 0
        self._rear = maxSize - 1
        self._qArray = [None] * maxSize
        
    def isEmpty(self):
        return self._count == 0
    
    def isFull(self):
        return self._count == len(self._qArray)
    
    def getSize(self):
        return self._count
    
    def enqueue(self, item):
        assert not self.isFull(), "Cannot enqueue to a full queue"
        self._rear = (self._rear + 1) % len(self._qArray)
        self._qArray[self._rear] = item
        self._count += 1
    
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        item = self._qArray[self._front]
        self._qArray[self._front] = None
        self._front = (self._front + 1) % len(self._qArray)
        self._count -= 1
        return item

    def getFront(self):
       assert not self.isEmpty(), "Cannot get the first element from an empty queue" 
       return self._qArray[self._front]
    
    def getRear(self):
        assert not self.isEmpty(), "Cannot get the last element from an empty queue"
        return self._qArray[self._rear]
#%%
'''
The circular array implementation improves the efficiency of these operations, but at the cost of limiting the size of the queue
A better solution is to use a linked list consisting of both front and rear reference
'''
#%%    
#Impementation of the Queue ADT using a linked list
class QueueNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._count = 0
    
    def isEmpty(self):
        return self._count == 0
    
    def getSize(self):
        return self._count
    
    def enqueue(self, item):
        node = QueueNode(item)
        if self.isEmpty():
            self._front = node
        else:
            self._rear.next = node
        self._rear = node
        self._count += 1
        
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        node = self._front
        if self._front is self._rear:
            self._rear = None
        self._front = self._front.next
        self._count -= 1
        return node.item
    
    def getFront(self):
        assert not self.isEmpty(), "Cannot get the first element from an empty queue" 
        return self._front.item
    
    def getRear(self):
        assert not self.isEmpty(), "Cannot get the last element from an empty queue"
        return self._rear.item  
#%%
 '''
Priority Queue
(1)a priority queue is a queue with each item is assigned a priority and items with a high priority are removed before those with lower priority
a.the bounded priority queue assumes a small limited range of p priorities over the interval of integers[0,p)
b.the unbounded priority queue places no limit on the range of integer values that can be used as priorities
c.integer values are used for the priorities with a smaller integer value having a higher pripority
(2)basic operations
a.PriorityQueue(): creates a new empty unbounded priority queue
a1.BPriorityQueue(numLevels): creates a new empty bounded priority queue with priority levels in the range from 0 to numLevels-1
b.isEmpty()
c.getSize()
d.enqueue(item, priority): adds the given item to the queue by inserting it in the proper position based on the given pripority
e.deququq(): removes and returns the front item from the queue, which is the item with the highest priority
             if two items have the same priority, then items are removed with FIFO order
'''
#%%             
#Implementation of the unbounded Priority Queue ADT using a Python list
class PriorityQEntry(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self._qList = list()
    
    def isEmpty(self):
        return len(self._qList) == 0
    
    def getSize(self):
        return len(self._qList)
    
    def enqueue(self, item, priority):
        entry = PriorityQEntry(item, priority)
        self._qList.append(entry)
        
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        #find the entry with the highest priority
        highest = self._qList[0].priority
        for i in range(self.getSize()):
            #see if the ith entry contains a higher priority(smaller integer)
            if self._qList[i].priority < highest:
                highest = self._qList[i].priority
        entry = self._qList.pop(highest)
        return entry.item
