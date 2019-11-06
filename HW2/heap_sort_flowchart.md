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
1.heap sort之程式是在理解概念與完成流程圖後，未參考任何資料的情況下自主寫出，代碼主要思路如下<br>
``` Python
def heap_sort(self, nums):
        max_heap = self.build_max_heap(nums)  #將未排序的nums建構成max-heap
        sorted_seq = []                      #建立sorted_seq記錄已排序的元素
        while len(max_heap) > 0:
            max_heap[0], max_heap[-1] = max_heap[-1], max_heap[0] #交換根節點與最後一個葉節點
            sorted_seq.insert(0, max_heap.pop())  #在max-heap中刪除最後一個葉節點，並將其插入sorted_seq的最前面（因先取出的節點較後取出的節點大）
            self.max_heapify(max_heap, 0)   #對新的根節點進行max-heapify
        return sorted_seq    
```



2.較為困難的是推導heap sort的時間複雜度以及過程中所用到的相關定理，如Master Theorem(主定理)<br>

