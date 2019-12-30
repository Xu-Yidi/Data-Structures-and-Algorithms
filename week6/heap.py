# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:53:55 2019

@author: Yidi
"""
# An array-based implementation of the max-heap
class MaxHeap:
    # Create a max-heap with maximum capacity of maxSize
    def __init__(self):
        self._elements = list()
        self._count = 0
    
    # Return the number of items in the heap
    def __len__(self):
        return self._count
    
    # Add a new value to the heap
    def add(self, value):
        # Add the new value to the end of the list
        self._elements.append(value)
        self._count += 1
        # Shift the new value up the tree
        self._shiftUp(self._count-1)
    
    # Extract the maximum value from the heap
    def extract(self):
        assert self._count > 0, "Cannot extract from an empty heap"
        # Save the root value and copy the last heap value to the root
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[-1]
        del self._elements[-1]
        #Shift the root value down the tree
        self._shiftDown(0)
        return value
        
    # Shift the value at the ndx element up the tree
    def _shiftUp(self, ndx):
        if ndx > 0:
            parent = ndx // 2
            if self._elements[ndx] > self._elements[parent]:
                # Swap elements
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
            self._shiftUp(parent)
    
    # Shift the value at the ndx element down the tree
    def _shiftDown(self, ndx):
        left = 2*ndx + 1
        right = 2*ndx + 2
        # Determine which node contains the larger value
        largest = ndx
        if left < self._count and self._elements[left] >= self._elements[largest]:
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx] 
            self._shiftDown(largest)

    def content(self):
        return self._elements



heap = MaxHeap()
for i in [-1,54,85,26,24,93,63,63,17,45]:
    heap.add(i)
