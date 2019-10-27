# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:54:32 2019

@author: Yidi
"""

#使用linked queue實作quick sort
#定義節點
class Node:
    def __init__(self, item): 
        self.item = item
        self.next = None
#定義包含quick sort操作的queue
class QuickSortQueue:
    def __init__(self):  #初始化queue的頭節點，尾節點以及元素個數
        self._front = None 
        self._rear = None
        self._count = 0
    
    def isEmpty(self):   #判斷queue是否為空，若元素個數為0，則queue為空
        return self._count == 0
    
    def getSize(self):   #返回queue中的元素個數
        return self._count
    
    def enqueue(self, item):  #在queue的結尾處插入新節點
        node = Node(item)     #生成新節點
        if self.isEmpty():    #如果queue為空，則新節點為頭節點
            self._front = node
        else:
            self._rear.next = node   #如果queue不為空，則將現在的尾節點指向新節點，並將新節點視為尾節點
        self._rear = node
        self._count += 1      #queue中的元素個數加1
        
    def dequeue(self):
        if self.isEmpty():    #如果queue為空，則無法刪除頭節點
            return "Cannot dequeue from an empty queue"
        node = self._front
        if self._front is self._rear: 
            self._rear = None
        self._front = self._front.next   #將queue中的原來的頭節點指向下一個節點視為新的頭節點
        self._count -= 1      #queue中的元素個數減1
        return node.item      #返回刪除的頭節點的值
    
    def getFront(self):       #若queue不為空，返回頭節點的值
        if self.isEmpty():
            return "Cannot get the first element from an empty queue" 
        return self._front.item
    
    def getRear(self):        #若queue中的元素不為空，返回尾節點的值
        if self.isEmpty():
            return "Cannot get the last element from an empty queue"
        return self._rear.item  
    
    def printitem(self):      #使用列表依序呈現queue中每個節點的值
        qitem = []
        node = self._front
        while node is not None:
            qitem.append(node.item)
            node = node.next
        return qitem
    
    def concatenation(self, seq): #將seq中刪除的頭結點插入queue的結尾，即將queue與seq連接
        while not seq.isEmpty():
            self.enqueue(seq.dequeue())
   
    def QuickSort(self):  
        if self.getSize() < 2:    #如果queue中的元素為0個或1個，則無需進行排序
            return
        pivot = self.getRear()    #將queue中的尾結點視為排序的基準點
        
        L = QuickSortQueue()      #建立三個新的queue以對此linked queue進行三分區間
        E = QuickSortQueue()
        G = QuickSortQueue()
        
        while not self.isEmpty(): #從queue的頭節點開始，將queue中的每個節點拿出與基準點比較，放入L,E或G，並在原來的queue中刪除節點
            n = self.getFront()   
            if n < pivot:
                L.enqueue(self.dequeue())   #將比pivot小的節點放入L,同時在原來的queue中刪除此節點
            elif n > pivot: 
                G.enqueue(self.dequeue())   #將比pivot大的節點放入G,同時在原來的queue中刪除此節點
            else: 
                E.enqueue(self.dequeue())   #將比pivot相等的節點放入E,同時在原來的queue中刪除此節點
        L.QuickSort()
        G.QuickSort()
        
        self.concatenation(L)  #將排序完成的queue連接起來
        self.concatenation(E)
        self.concatenation(G)

solution = QuickSortQueue()       
for i in [54,85,85,26,24,93,63,17,45]:
    solution.enqueue(i)
solution.QuickSort()                
solution.printitem()   
   
