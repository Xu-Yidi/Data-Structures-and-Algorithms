### Merge Sort V.S. Heap Sort

| Alogrithm | Time Complexitiy | Space Complexity | Stability |
| :-: | :-: | :-: | :-: |
| Merge Sort |Best/Worst/Average case: O(nlogn)| O(n) | Stable |
| Heap Sort |Best/Worst/Average case: O(nlogn) | O(1) | Unstable|

- **Time Complexitiy**<br>

1.merge sort和heap sort在最佳、最壞及平均情況下的時間複雜度均為O(nlogn)，說明此兩種排序方法花費的時間並不會因輸入資料的改變而有差異<br>
2.merge sort的時間複雜度分析<br>
>(1)merge sort總時間 = 分解時間 + 子序列排序時間 + 合併時間，因為分解時間可視為常數，即時間複雜度為O(1)，故可忽略不計，則merge sort總時間 = 子序列排序時間 + 合併時間<br>
>(2)假設一有n個元素的序列的排序時間為T(n)，T(n) = 2T(n/2) + an，其中T(n/2)為一個子序列的排序時間，an為合併時間，可由遞迴的形式推導得到T(n)=O(nlogn)<br>

3.heap sort的時間複雜度分析<br>
>(1)heap sort的時間複雜度主要包含建構max-heap以及每次取走最大值後重新max-heapify的過程，其中建構max-heap的時間複雜度為O(n)，取走最大值並重建堆的時間複雜度為(n-1)logn，故總時間複雜度T(n) = O(n) + (n-1)logn = O(nlogn)

- **Space Complexity**<br>

space complexity為空間複雜度，是衡量算法執行時所需要的記憶體空間，而時間複雜度和空間複雜度有時並不可兼得<br>
1.merge sort的空間複雜度為為O(n)，即merge sort不是原地排序算法，因為合併過程需要與原始序列相同數量級的儲存空間存放合併結果，需要注意的是雖然merge sort的遞迴次數是logn，但遞迴完成後會釋放占用的記憶體空間，故所需空間不會累加<br>
2.heap sort的空間複雜度為O(1),即heap sort是原地排序<br>

- **Stability**<br>

Stability為穩定性，其意義為待排序的序列中有多個相等的元素，經過排序後其先後順序保持不變<br>
1.merge sort為穩定算法<br>
2.heap sort為不穩定算法<br>








- **Reference**<br>
詳談歸併排序時間複雜度分析https://blog.csdn.net/liangjiabao5555/article/details/89670082<br>
排序算法之 堆排序 及其時間複雜度和空間複雜度https://blog.csdn.net/YuZhiHui_No1/article/details/44258297<br>
排序算法時間複雜度、空間複雜度、穩定性比較https://blog.csdn.net/yushiyi6453/article/details/76407640<br>

- **可參考之文檔**<br>
https://www.cs.auckland.ac.nz/compsci220s1c/lectures/2016S1C/CS220-Lecture09.pdf (主要內容為merge sort時間複雜度的計算過程)<br>
http://disi.unitn.it/~rseba/DIDATTICA/dsa2011_BZ/dsa04.pdf (主要內容包含heap sort時間複雜度的計算過程)<br>
https://subetter.com/algorithm/understand-and-compute-algorithmic-complexity.html (主要內容包含求解遞迴函數時間複雜度的定理）<br>
