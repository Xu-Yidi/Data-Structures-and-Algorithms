# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:44:24 2019

@author: Yidi
"""
'''
Quick Sort
The quick-sort algorithm sorts a sequence S using a simple recursiv approach. The main idea is to apply the divide-and-conquer technique, 
whereby we divide S into subsequences, recur to sort each subsequence, and then combine the sorted subsequences by a simple concatenation

Logic
1.Divide: If Seqence S has at least two elements, select a specific element x from s, 
called the pivot(usually the last element in S). Partition the sequence S into three subsequences:
(1)Less(Left): store the elements in S less than pivot x
(2)Equal: store the elements in S equal to pivot x
(3)Greater(Right): store the elements in S greater than pivot x
2.Conquer: Recurxively sort subsequences Less and Greater.
3.Combine: Combine the sorted subsequenes by a simple concatenation
'''
def quick_sort(seq):
    # Nothing need to be done if the sequence has zero or one element
    n = len(seq)
    if n < 2:
        return seq
    
    # select the last element in the sequence as the pivot
    pivot = seq[-1]
    #print(pivot)
    
    # Partition the sequence into three subseqences
    less = []
    equal = []
    greater = []
    
    for temp in seq:
        if temp < pivot:
            less.append(temp)
        elif temp == pivot:
            equal.append(temp)
        else:
            greater.append(temp)
    
    # Recursively sort the subsequences less and greater and combine then using the operator "+" 
    return quick_sort(less) + equal + quick_sort(greater) 
seq = [54,26,93,17,20,77,31,44,55,20]
quick_sort(seq)
#%%
'''
An algorithm is **in-place**(原地置换) if it uses only a small amount of memory in addition to that needed for the original input. 
The implementation of quick-sort showed above does not qualify as in-place because we use additional containers L, E, and G when dividing a sequence S within each recursive call. 
In-place quick-sort doee not create additional subsequences but using **element swapping** to modify original input sequence. 
Local variables *left*, which advances rightward, and *right*, which advances leftward, will be used to scan the sequence simultaneously and swap pairs of elements in reverse order. 
When the two indices pass each other, the division step is complete.
'''

def inplace_quick_sort(seq, a , b):
    if a >= b: #range is trivially sorted
        return
    
    pivot = seq[b] #select last element as pivot
    left = a #scan the element rightward
    right = b - 1 #scan the element leftward
    
    while left <= right:
        #scan until reaching an element lagger than pivot
        while left <= right and seq[left] <= pivot:
            left += 1
        while left <= right and pivot <= seq[right]:
            right -= 1
        if left <= right:
            seq[left], seq[right] = seq[right], seq[left]
            left, right = left + 1, right - 1
    seq[left], seq[b] = seq[b], seq[left]
        
    inplace_quick_sort(seq, a, left - 1)
    inplace_quick_sort(seq, left + 1, b)
    return seq
#%%
def quicksort(seq,p,r):
	if p < r:
		q = partition(seq,p,r)
		quicksort(seq,p,q)
		quicksort(seq,q+1,r)

def partition(seq, p, r):
	i = p - 1
	for j in range(p, r):
		if seq[j] <= seq[r]:
			i += 1
			seq[i], seq[j] = seq[j], seq[i]
	seq[i+1], seq[r] = seq[r],seq[i+1]
	return i
list1=[2,2,8,7,1,3,5,6,4]
quicksort(list1,0,len(list1)-1)


