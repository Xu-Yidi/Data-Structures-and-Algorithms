# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:04:36 2019

@author: Yidi
"""

'''
Insertion Sort
1.logic:
(1)partition the array into two regions: sorted and unsorted
(2)take each item from the unsorted region and insert it into its correct order in the sorted region
2.advantages and disadvantages
(1)adaptive, i.e. efficient for nearly-sorted datasets
(2)in-place, i.e. requires a constant O(1) of additional memory space
(3)slow for unsorted or reverse-sorted data
(4)needs a large number of element shifts
'''
#%%
#Sorts a sequence in ascending order using the insertion sort algorithm
def insertionSort(theSeq):
    n = len(theSeq)
    #starts with the first item as the only sorted entry
    for i in range(1, n):
        #save the value to be positioned
        value = theSeq[i]
        #find the position where value fits in the ordered part of the list
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            #shift the items to the right duing the research
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        #put the saved value into the open slot   
        theSeq[pos] = value
        
    return theSeq

a = [3,6,2,7,5,9,4,6,1]        
insertionSort(a)
#%%       
 '''
Bubble Sort
1.logic:
(1)go through multiple passes over the array
(2)in every pass:
a.compare adjacent elements in the list
b.exchange the elements if they are out of order
c.each pass moves the largest(or smallest) elements to the end of the array 
(2)repeating this process in several passes eventually sorts the array into ascending(or descending) order
'''     
#%%        
#Sorts a sequence in ascending order using the bubble sort algorithm
def bubbleSort(theSeq):
    n = len(theSeq)
    #peform n-1 bubble operations on the sequence
    for i in range(n-1):
        #bubble the largest item to the end
        for j in range(n-1-i):
            if theSeq[j] > theSeq[j + 1]:
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1] #swap the j and j+1 items
                theSeq[j + 1] = tmp
    return theSeq

a = [3,6,2,7,5,9,4,6,1]        
bubbleSort(a)
#%%
'''
Selection Sort
1.logic
(1)choose the largest/smallest item in the array and place the item in its correct place
(2)choose the next largest/next smallest item in the array and place the item in its correct place
(3)repeat the process until all items are sorted
2.does not depend on the initial arrangement of the data 
'''
#%%
#Sorts a seqence in ascending order using the selection sort algorithm
def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n-1):
        #assum the ith element is the smallest
        smallNdx = i
        #determine if any other element contains a smaller value
        for j in range(i+1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
        #swap the ith value and smallNdx value only if the smallest value is 
        #not already in its proper position
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp
    return theSeq

a = [3,6,2,7,5,9,4,6,1]        
selectionSort(a)
