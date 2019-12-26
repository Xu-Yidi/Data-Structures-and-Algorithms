[code-insertion sort & bubble sort & selection sort的實現](/week4/handout-sorting.py)
### Insertion Sort
- **Logic**<br>
1.partition the array into two regions: sorted and unsorted<br>
2.take each item from the unsorted region and insert it into its correct order in the sorted region<br>
- **Advantages and Disadvantages**<br>
1.adaptive, i.e. efficient for nearly-sorted datasets:smiley:<br>
2.in-place, i.e. requires a constant O(1) of additional memory space:smiley:<br>
3.slow for unsorted or reverse-sorted data:cry:<br>
4.needs a large number of element shifts:cry:<br>
- **Leetcode**<br>
[#147 insertion sort list](/week4/%23147%20insertion%20sort%20list.py)<br>

### Bubble Sort
- **Logic**<br>
1.go through multiple passes over the array<br>
2.in every pass:<br>
>>(1)compare adjacent elements in the list<br>
>>(2)exchange the elements if they are out of order<br>
>>(3)each pass moves the largest(or smallest) elements to the end of the array<br> 
3.repeating this process in several passes eventually sorts the array into ascending(or descending) order<br>

### Selection Sort
- **Logic**<br>
1.choose the largest/smallest item in the array and place the item in its correct place<br>
2.choose the next largest/next smallest item in the array and place the item in its correct place<br>
3.repeat the process until all items are sorted<br>

### Time Complexity
- **Asymptotic Notation(漸進符號)**<br>
<img height="75%" width="75%" src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week4/time_complexity1.JPG"><br>

- **The Most Common Time Complexities**<br>
<img height="75%" width="75%" src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week4/time_complexity2.jpeg"><br>

| Name | Time Complexity | Class|
| :-: | :-: | :-:|
| Constant time | O(1) | Polynomial time |
| Logarithmic time | O(logn) | Polynomial time |
| Linear time | O(n) | Polynomial time |
| Quasilinear time| O(nlogn)| Polynomial time |
| Quadratic time| O(n^2) | Polynomial time |
| Exponential time| O(2^n) | Non-deterministic polynomial time |
| Factorial time| O(n!) | Non-deterministic polynomial time |

- **How to Calculate Time Complexity**<br>

| Algorithm | Best Case | Average Case| Worst Case |
| :-: | :-: | :-:| :-: |
| Bubble Sort | O(n^2)/O(n) | O(n^2) | O(n^2) |
| Selection Sort | O(n^2) | O(n^2) | O(n^2) |
| Insertion Sort | O(n) | O(n^2) | O(n^2) |
| Quick Sort| O(nlogn)| O(nlogn) | O(n^2) |

<img height="75%" width="75%" src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week4/time_complexity3.JPG"><br>
<img height="75%" width="75%" src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week4/time_complexity4.JPG"><br>
 
 1.Big-O-Notation Rules<br>
 >>(1)**`Transitivity rule`**<br>
 >>If *f*(n) ∈ O(*g*(n)) and *g*(n) ∈ O(*h*(n)), then *f*(n) ∈ O(*h*(n))<br>
 >>(2)**`Addition rule`**<br>
 >>If *f*(n) ∈ O(*g*(n)) and *g*(n) ∈ O(*h*(n)), then *f*(n) + *g*(n) ∈ O(max(*g*(n),*h*(n)))<br>
 >>(3)**`Multiplication Rule`**<br>
 >>If *f*(n) ∈ O(*g*(n)) and *g*(n) ∈ O(*h*(n)), then *f*(n) * *g*(n) ∈ O(*g*(n) * *h*(n))<br>
[proof](https://www.cs.hmc.edu/~keller/cs60book/11%20Complexity.pdf)<br>

- **reference**<br>
[Complexity: Asymptotic Notation(漸進符號)](http://alrightchiu.github.io/SecondRound/complexityasymptotic-notationjian-jin-fu-hao.html)<br>
[知乎-如何清晰的理解算法中的时间复杂度？](https://www.zhihu.com/question/20196775)<br>
[CSDN-算法的时间复杂度和空间复杂度-总结](https://blog.csdn.net/zolalad/article/details/11848739)<br>
