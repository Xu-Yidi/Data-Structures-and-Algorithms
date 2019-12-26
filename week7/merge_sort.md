[code-merge sort自己撰寫的程式與參考程式](/week7/merge_sort_04151702.py)
### Merge Sort
As quick sort, merge sort use recursion in an algorithm design called **divide-and-conquer**, so what's divide-and-conquer technique?<br>
- **Divide-and-conque**<br>
1.***Divide***: If the input size is smaller than a certain threshold(say, one or two element), solve the problem directly using a straightforward method and return the solution so obtained. Otherwise, divide the input data into two or more disjoint subsets<br>
2.***Conquer***: Recursively solve the subproblems associated with the subsets<br>
3.***Combine***: Take the solutions to the subproblems and merge them into a solution to the original problem<br>
- **Logic**<br>
To sort a sequence S with n elements using the three divide-and-coquer steps, the merge-sort algorithm proceeds as follows:<br>
1.***Divide***: If S has zero or one element, return S immediately; it is already sorted. Otherwise(S has at least two elements), remove all the elements from S and put them into two sequences, S1 and S2, each containing about half of the elements of; that is, S1 contaings the first *floor(n/2)* elements of S, and S2 contains the remaining *ceil(n/2)* elements<br>
2.***Conquer***: Recursively sort sequences S1 and S2<br>
3.***Combine***: Put back the elements into S by merging the sorted sequence S1 and S2 into a sorted sequence<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week7/merge_sort1.jpg">
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week7/merge_sort2.jpg">

- **Time Complexities**<br>
1.best case: O(nlogn)<br>
2.worst case:O(nlogn)<br>
3.average case:O(nlogn)<br>
