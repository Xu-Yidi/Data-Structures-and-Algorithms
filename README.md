# **Data Structure and Algorithm in Python**
此處文件包含自行整理之資料結構的handout與Leetcode的程式，handout包含資料結構的基本特性的描述（以註解方式給出）以及基本操作的Python程式<br>
## Content
 [Week2(singly linked list)](#week2)<br>
 [Week3(stack & queue)](#week3)<br>
 [Week4(insertion sort & bubble sort & selection sort & time complexities)](#week4)<br>
 [Week5(quick sort)](#week5)<br>
 [Week6(heap sort)](#week6)<br>
 
## Week2
### Singly Linked List
[code-linked list的基本操作](/week2/handout-singly%20linked%20list.py)<br>
- **Linked List**<br>
1.A linked structure contains a collection of objects called nodes, each of which contains data and at least one reference or link to another node<br>
2.A linked list is a structure in which the nodes are connected in sequence to form a linear list<br>
>>(1)The first node in the list(***head node***), must be named or referenced by external variable<br>
>>(2)The last node in the list(***tail node***), is indicated by a null link reference<br>
>>(3)A linked list can be empty, which can be indicated when the head reference is null<br>
- **The Singly Linked List**<br>
1.a singly linked list is a linked list in which each node contains a single link field and allows for a complete traversal from a distinctive first node to the last<br>
- **LeetCode**<br>
[#707 design linked list](/week2/%23707%20design%20linked%20list.py)<br>
[#206 reverse linked list](/week2/%23206%20reverse%20linked%20list.py)<br>

[back to content](#content)<br>

## Week3
### Stack
[code-stack的array與linked list實現](/week3/handout-stack.py)<br>
- **The Stack ADT**<br>
1.inserted and removed sccording to the ***last-in, first-out(LIFO) principle***<br>
2.***top*** of the stack/ ***base*** of the stack<br>
3.basic operations:<br>
>>(1)**`isEmpty()`**: returna boolean value indicating if the stack is empty<br>
>>(2)**`getSize()`**: returns the number of items in the stack<br>
>>(3)**`pop()`**: remove and returns the top item of the stack, if the stack is not empty, and the next item on the stack becomes the new top item<br>
>>(4)**`push(item)`**: adds the given item to the top of the stack<br>
>>(5)**`peek()`**: returns a reference to the item on top of a non-empty stack without removing it<br>
- **Implementing the Stack**<br> 
1.the stack ADT can be implemented by the use of Python list and a linked list<br>
- **LeetCode**<br>
[#155 min stack](/week3/%23155%20min%20stack.py)<br>

### Queue
[code-circular queue的array與linked list實現&priority queue的array實現](/week3/handout-queue.py)<br>
- **The Queue ADT**<br>
1.items can only be added to one end and removed from the other, known as the ***first-in, first-out(FIFO)principle***<br>
2.new items are inserted into a queue at the ***rear*** while existing items are removed from the ***front***<br>
3.basic operations:<br>
>>(1)**`isEmpty()`**: return a boolean value indicating whether the queue is empty<br>
>>(2)**`getSize()`**: returns the number of items currently in the queue<br>
>>(3)**`enqueue(item)`**: adds the given item to the back of the queue<br>
>>(4)**`dequeue()`**: removes and returns the front item from the queue, an item can not be dequeued from an empty queue<br>
>>(5)**`getFront()`**: return a reference to the element at the front of queue without removing it, and an error occurs if the queue is empty<br>
>>(6)**`getRear()`**: return a reference to the element at the back of queue without removing it<br>
- **Implementing the Queue**<br>
1.implementation of the Queue ADT using a Python list<br>
2.**using a circular array**<br>
(1)a circular array is simply an array viewed as a circle instead of a line<br>
(2)allows to add new items to a queue and remove existing ones without having to shift items in the process<br>
(3)introduces the concept of a ***maximum-capacity queue*** that can become full<br>
(4)uesd with application that require small-capacity and allows for the specification of a maximum size<br>
(5)must maintain a count field and two markers:<br>
>>a.***count field***: to keep track of how many items are currently in the queue<br>
>>b.***front and rear***: to indicate the array elements containing the first and last items in the queue<br>
- **The Priority Queue**<br>
1.a priority queue is a queue with each item is assigned a priority and items with a high priority are removed before those with lower priority<br>
(1)***the bounded priority queue*** assumes a small limited range of p priorities over the interval of integers[0,p)<br>
(2)***the unbounded priority queue*** places no limit on the range of integer values that can be used as priorities<br>
(3)integer values are used for the priorities with a smaller integer value having a higher pripority<br>
2.basic operations:<br>
>>(1)**`PriorityQueue()`**: creates a new empty unbounded priority queue<br>
>>(or 1)**`BPriorityQueue(numLevels)`**: creates a new empty bounded priority queue with priority levels in the range from 0 to numLevels-1<br>
>>(2)**`isEmpty()`**<br>
>>(3)**`getSize()`**<br>
>>(4)**`enqueue(item, priority)`**: adds the given item to the queue by inserting it in the proper position based on the given pripority<br>
>>(5)**`deququq()`**: removes and returns the front item from the queue, which is the item with the highest priority,if two items have the same priority, then items are removed with FIFO order<br>
- **LeetCode**<br>
[#232 implement queue using stacks](/week3/%23232%20implement%20queue%20using%20stacks.py)<br>
[#622 design circular queue](/week3/%23622%20design%20circular%20queue.py)<br>

[back to content](#content)<br>

## Week4
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

[back to content](#content)<br> 

## Week5
[code-quick sort使用額外空間與原地置換的實現](/week5/handout-quick_sort.py)
### Quick Sort
The quick-sort algorithm sorts a sequence S using a simple **recursiv** approach. The main idea is to apply the **divide-and-conquer** technique, whereby we divide S into subsequences, recur to sort each subsequence, and then combine the sorted subsequences by a simple concatenation<br>
- **Logic**<br>
1.**Divide**: If Seqence S has at least two elements, select a specific element x from s, called the pivot(usually the last element in S). Partition the sequence S into three subsequences:<br>
(1)***Less(Left)***: store the elements in S less than pivot x<br>
(2)***Equal***: store the elements in S equal to pivot x<br>
(3)***Greater(Right)***: store the elements in S greater than pivot x<br>
2.**Conquer**: Recurxively sort subsequences Less and Greater.<br>
3.**Combine**: Combine the sorted subsequenes by a simple concatenation<br>
- **Time Complexities**<br>
<img height="75%" width="75%" src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week5/quick_sort.JPG"><br>
<img height="75%" width="75%" src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week5/quick_sort2.JPG"><br>
[back to content](#content)<br> 

## Week6
### The Heap Data Struture
- The (Binary) heap *T* is an **array** object that can be viewed as a nearly **complete binary tree(完全二元樹)** and satisfies two additional properties: a relation property defined in terms of the ways are stored in *T* and a structural property defined in terms of the shape of *T* itself.<br>
>>(1)**Heap-Order Property(relational property)**: In a heap *T*, for every position *p* other than the root, the key sorted at *p* is geater than or equal to the key stored at *p*'s parent.<br>
>>(2)**Complete Binary Tree Property(strutural property)**: A heap *T* with height *h* is a complete binary tree if levels 0,1,...,*h*-1 of *T* have the maximum numbers of nodes possible(i.e. level *i* has 2^*i* nodes, for 0 ≤ *i* ≤ *h*-1) and the remaining nodes at level *h* reside in the leftmost possible at that level.<br>

- The **height** of a node in a heap is the number of edges on the longest simple downward path from the node to a leaf, and the height of the heap to be the height of the root.<br>
>>(1)A heap *T* storing n entries has height ***h* = floor(log_2(*n*))**<br>
>>(2)For example:<br>
the height of the heap is 3(a heap with height *h* has *h+1* levels)<br>
the height of the node 1 is 2<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week6/min_heap.png">

- If a complete binary tree with n nodes is represented sequentially, then for any node with index *i*, 0 ≤ *i* ≤ *n*-1, we have:
>>(1)A[0] is the root of the tree<br>
>>(2)the parent of node i: **parent(i) = floor((i-1)/2)**<br>
>>(3)the left child of node i: **left(i) = 2i + 1**<br>
>>(4)the right child of node i: **right(i) = 2i + 2**<br>

- Heap properties:<br>
>(1)**Max-heap**:the largest element in a max-heap is at the root and the subtree rooted at a node contains values no larger than that contained at the node itself, i.e. A[parent(i)] >= A[i].<br>
>(2)**Min-heap**:the smallest element in a min-heap is at the root and subtree rooted at a node contains values no smaller than that contained at the node itself, i.e. A[parent(i)] <= A[i]<br>

### Basic Operations**
1.**shift-up**(insertion): to restore the heap order property, the new value has to move up along the path in reverse order from the root to the insertion point until a node is found where it can be positioned properly.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week6/shift-up.jpg">




[back to content](#content)<br>
