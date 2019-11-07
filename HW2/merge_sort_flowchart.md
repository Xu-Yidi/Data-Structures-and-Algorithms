### Merge sort
Merge sort和Quick sort同屬Divide-and-conquer(分治法)的應用<br>
- **Logic**<br>
1.***Divide***:如果資料序列*S*只有一個或者0個元素，則無需進行排序；否則將*S*中的元素分別放入兩個子序列*S1*和*S2*中，*S1*和*S2*各占一半元素<br>
2.***Conquer***:遞迴地對*S1*和*S2*進行排序<br>
3.***Combine***:將排序好的*S1*和*S2*進行合併(Merge sort的重點即在於合併)<br>
- **Flowchart**<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week7/merge_sort_flowchart.jpg">

- **Time complexities**<br>
The running time of mergesort on an input list of size n is **O(nlogn)** in the best, worst, and average case<br>
- **學習歷程**<br>
在理解merge sort的概念後嘗試自主寫出程式，但過程相較heap sort可謂艱難許多，最主要的原因是因為對遞迴寫法的掌握度




