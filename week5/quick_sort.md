[code-quick sort使用額外空間與原地置換的實現](/week5/handout-quick_sort.py)
### Quick Sort
The quick-sort algorithm sorts a sequence S using a simple **recursive** approach. The main idea is to apply the **divide-and-conquer** technique, whereby we divide S into subsequences, recur to sort each subsequence, and then combine the sorted subsequences by a simple concatenation<br>
- **Logic**<br>
1.**Divide**: If Seqence S has at least two elements, select a specific element x from s, called the pivot(usually the last element in S). Partition the sequence S into three subsequences:<br>
(1)***Less(Left)***: store the elements in S less than pivot x<br>
(2)***Equal***: store the elements in S equal to pivot x<br>
(3)***Greater(Right)***: store the elements in S greater than pivot x<br>
2.**Conquer**: Recurxively sort subsequences Less and Greater.<br>
3.**Combine**: Combine the sorted subsequenes by a simple concatenation<br>
- **Example**
<img src="/week5/quick_sort_flowchart_example.jpg">

- **Time Complexities**<br>
<img height="75%" width="75%" src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week5/quick_sort.JPG"><br>
<img height="75%" width="75%" src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week5/quick_sort2.JPG"><br>
