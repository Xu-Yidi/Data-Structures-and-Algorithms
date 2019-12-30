# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:34:21 2019

@author: Yidi
"""


class Solution(object):
    def heap_sort(self, nums):
        max_heap = self.build_max_heap(nums)  #將未排序的nums建構成max-heap
        sorted_seq = []                      #建立sorted_seq記錄已排序的元素
        while len(max_heap) > 0:
            max_heap[0], max_heap[-1] = max_heap[-1], max_heap[0] #交換根節點與最後一個葉節點
            sorted_seq.insert(0, max_heap.pop())  #在max-heap中刪除最後一個葉節點，並將其插入sorted_seq的最前面（因先取出的節點較後取出的節點大）
            self.max_heapify(max_heap, 0)   #對新的根節點進行max-heapify
        return sorted_seq    
    

    def max_heapify(self, subseq, i):   #節點的index從0開始
        if 2*i + 1 >= len(subseq):      #如果節點左子節點的index已經大於等於subseq的長度，則節點為葉節點，無需進行max-heapify
            return
        big_child_index = 2*i + 1       #預設節點的左子節點是其兩個子節點中較大的
        big_child_val = subseq[2*i + 1]
        if 2*i + 2 < len(subseq):       #如果節點的右子節點存在（節點可能只存在左子節點），即右子節點的index小於subseq的長度
            if subseq[2*i + 2] > big_child_val:  #如果右子節點的值大於左子節點的值，則右子節點為兩個子節點中較大的
                big_child_index = 2*i + 2
                big_child_val = subseq[2*i + 2]
        if subseq[i] < big_child_val:   #如果節點小於其子節點中較大的節點，則將二者進行交換
            subseq[big_child_index] = subseq[i]
            subseq[i] = big_child_val
        self.max_heapify(subseq, big_child_index)  #交換後原節點的index變為較大子節點的index，不斷進行max-heapify的過程直至節點交換到正確位置


    def build_max_heap(self, seq):
        nf_index = int(len(seq)/2) - 1  #葉節點(non-leaf node)的index為floor(n/2))至n-1，無需進行max-heapify
        while nf_index >= 0:            #從底層的非葉節點開始，對每一個非葉節點進行max-heapify直至根節點為止    
            self.max_heapify(seq, nf_index)
            nf_index -= 1
        return seq                     #返回最終的max-heap

output = Solution().heap_sort([-1,54,85,26,24,93,63,63,17,45])
output


