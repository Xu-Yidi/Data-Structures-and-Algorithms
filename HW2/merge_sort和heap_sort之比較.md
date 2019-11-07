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







- **Reference**<br>
詳談歸併排序時間複雜度分析https://blog.csdn.net/liangjiabao5555/article/details/89670082<br>

- **可參考之文檔**<br>
https://www.cs.auckland.ac.nz/compsci220s1c/lectures/2016S1C/CS220-Lecture09.pdf
