### The Heap Data Struture
- The (Binary) heap *T* is an **array** object that can be viewed as a nearly **complete binary tree(完全二元樹)** and satisfies two additional properties: a relation property defined in terms of the ways are stored in *T* and a structural property defined in terms of the shape of *T* itself.<br>
>(1)**Heap-Order Property(relational property)**: In a heap *T*, for every position *p* other than the root, the key sorted at *p* is geater than or equal to the key stored at *p*'s parent.<br>
>(2)**Complete Binary Tree Property(strutural property)**: A heap *T* with height *h* is a complete binary tree if levels 0,1,...,*h*-1 of *T* have the maximum numbers of nodes possible(i.e. level *i* has 2^*i* nodes, for 0 ≤ *i* ≤ *h*-1) and the remaining nodes at level *h* reside in the leftmost possible at that level.<br>

- The **height** of a node in a heap is the number of edges on the longest simple downward path from the node to a leaf, and the height of the heap to be the height of the root.<br>
>(1)A heap *T* storing n entries has height ***h* = floor(log_2(*n*))**<br>
>(2)For example:<br>
the height of the heap is 3(a heap with height *h* has *h+1* levels)<br>
the height of the node 1 is 2<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week6/heap.jpg">

- If a complete binary tree with n nodes is represented sequentially, then for any node with index *i*, 0 ≤ *i* ≤ *n*-1, we have:
>(1)A[0] is the root of the tree<br>
>(2)the parent of node i: **parent(i) = floor((i-1)/2)**<br>
>(3)the left child of node i: **left(i) = 2i + 1**<br>
>(4)the right child of node i: **right(i) = 2i + 2**<br>

- Heap properties:<br>
>(1)**Max-heap**:the largest element in a max-heap is at the root and the subtree rooted at a node contains values no larger than that contained at the node itself, i.e. A[parent(i)] >= A[i].<br>
>(2)**Min-heap**:the smallest element in a min-heap is at the root and subtree rooted at a node contains values no smaller than that contained at the node itself, i.e. A[parent(i)] <= A[i]<br>

### Basic Procedures
- **shift-up**(insertion): To restore the heap order property, the new value has to move up along the path in reverse order from the root to the insertion point until a node is found where it can be positioned properly.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week6/shift-up.jpg">

- **shift-down**(remove): After the value in the root has been removed, the value from the rightmost node on the lowest level is copied to the root and that leaf is removed. Then starting at the root node, the node's value is compared to its children and swapped with the larger of the two, and this process continues until the smaller value is copied into a leaf node or a node whose children are even smaller.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week6/shift-down.jpg">

- **max-heapify**: Given an array A and an index i, assume the binary trees rooted at **left(i)** and **right(i)** are max heaps, but A[i] may be smaller than its children. Then the value at A[i] float down in the max-heap until the subtree rooted at index i becomes a max heap.<br>
<img src = "https://github.com/Xu-Yidi/fluteanzi/blob/master/week6/max-heapify.jpg">

- **build-max-heap**: We can use the max-heapify procedure to convert an array A[0,1,...,n-1] into a max-heap in a **bottom-up** manner. The elements in the subarray A[floor(n/2),...,n-1] are **leaves** of the tree, and so each is a 1-element heap. The procedure build-max-heap goes through the remaining nodes of the tree and runs max-heapify on each one.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week6/build-max-heap1.jpg">
detailed process<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week6/build-max-heap2.jpg">
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week6/build-max-heap3.jpg">

### Heap Sort
- **Logic**<br>
1.Build a **max-heap** from the unorderes array<br>
2.Starting with the root(the maximum element), the algorithm places the maximum element into the correct place in the array by **swapping it with the element in the last position** in the array<br>
3.**"Discard" this last node**(knowing that it's in its correct place) by decreasing the heap size, and calling max-heapify on the new(possibly incorrectly-placed) root<br>
4.Repeating this "discarding" process until only one node(the smallest element) remains, and therefore is in the correct place in the array<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week6/heap_sort1.jpg">
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week6/heap_sort2.jpg">

- **Time Complexities**<br>
1.max-heapify:O(logn)<br>
2.build-max-heap:O(n)<br>
3.heap sort:O(nlogn)(best/worst/average case)<br>
