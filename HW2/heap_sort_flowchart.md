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
1. max-heapify: O(logn)<br>
2. build-max-heap: O(n)<br>
3. heap sort: O(nlogn)<br>

- **學習歷程**<br>
1.heap sort之程式是在理解概念與完成流程圖後，未參考任何資料的情況下自主寫出<br>
2.較為困難的是推導heap sort的時間複雜度以及過程中所用到的相關定理，如Master Theorem(主定理)<br>

