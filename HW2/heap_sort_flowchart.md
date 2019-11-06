### Heap sort
事實上，為更嚴謹地介紹heap sort之觀念，應先介紹heap(堆積)的資料結構與其基本操作，但為使篇幅不過於冗長，這部分整理在Github上Week6的學習筆記中，可至此處詳閱
[Heap(堆積)資料結構以及max-heapify/build-max-heap等基本操作](https://github.com/Xu-Yidi/fluteanzi/blob/master/README.md#week6)
- **Logic**<br>
1.將未排序之資料建構成max-heap(最大堆)之形態（通過對非葉節點進行max-heapify之操作）<br>
2.將根節點與最底層最右邊之葉節點進行交換<br>
3.刪除最底層最右邊之葉節點，即原來之根節點，並對新的根節點進行max-heapify之操作<br>
4.重複上述2及3之操作，直至排序完成<br>

- **Flowchart**<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week6/heap_sort.png">

- **Time Complexities**<br>
1.max-heapify: O(logn)<br>
2.build-max-heap: O(n)<br>
3.heap sort: O(nlogn)<br>

- **學習歷程**<br>
heap sort之程式是在理解概念與完成流程圖後，未參考任何資料的情況下自主寫出，較為困難的是推導heap sort的時間複雜度以及過程中所用到的相關定理，代碼主要思路如下<br>

``` Python
class Solution():
    def heap_sort(self, nums):
        max_heap = self.build_max_heap(nums)  #將未排序的nums建構成max-heap
        sorted_seq = []                      #建立sorted_seq記錄已排序的元素
        while len(max_heap) > 0:
            max_heap[0], max_heap[-1] = max_heap[-1], max_heap[0] #交換根節點與最後一個葉節點
            sorted_seq.insert(0, max_heap.pop())  #在max-heap中刪除最後一個葉節點，並將其插入sorted_seq的最前面（因先取出的節點較後取出的節點大）
            self.max_heapify(max_heap, 0)   #對新的根節點進行max-heapify
        return sorted_seq    
```
上述片段是實現heap sort的主要代碼，在呼叫build_max_heap函數構造最大堆後，將根節點與最後一個葉節點交換並刪除最後的葉節點,再對新的根節點運行max_heapify函數，直至排序完成
```Python
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

```
上述片段定義了實現max-heapify的函數，其主要做法是先通過比較該節點的左右節點，找出較大的子節點，然後比較該節點與較大子節點的大小，若該節點比較大子節點小，則交換二者位置，且函數使用recursive的寫法使該節點不斷與其子節點比較並shift down至正確位置
```Python
   def build_max_heap(self, seq):
        nf_index = int(len(seq)/2) - 1  #葉節點(non-leaf node)的index為floor(n/2))至n-1，無需進行max-heapify
        while nf_index >= 0:            #從底層的非葉節點開始，對每一個非葉節點進行max-heapify直至根節點為止    
            self.max_heapify(seq, nf_index)
            nf_index -= 1
        return seq                     #返回最終的max-heap
```
上述片段則是定義了實現build-max-heap的函數，其主要是通過對非葉節點進行max-heapify實現的
```Python
output = Solution().heap_sort([-1,54,85,26,24,93,63,63,17,45])
output
Out[275]: [-1, 17, 24, 26, 45, 54, 63, 63, 85, 93]
```
測試成功<br>
- **思考**<br>
heap sort中額外使用sorted_seq來儲存已經排序之元素，且在leetcode上經過測試後其耗時較久，可思考如何修改程式使其不需額外空間並節省時間
