# **Data Structure and Algorithm in Python**
此處文件包含自行整理之資料結構的handout與Leetcode的程式，handout包含資料結構的基本特性的描述（以註解方式給出）以及基本操作的Python程式<br>
[Git語言入門](https://zhuanlan.zhihu.com/p/30044692)
## Content
 [Week2(singly linked list)](#week2)<br>
 [Week3(stack & queue)](#week3)<br>
 [Week4(insertion sort & bubble sort & selection sort & time complexities)](#week4)<br>
 [Week5(quick sort)](#week5)<br>
 [Week6(heap data structure & heap sort)](#week6)<br>
 [Week7(merge sort)](#week7)<br>
 [Week8(binary tree)](#week8)<br>
 [Week9(binary search tree)](#week9)<br>
 [Week10(red-black trees)](#week10)<br>
 [Week11(hash tables)](#week11)<br>
 [Week12&13(breadth-first search/depth-first search)](#week12&13)<br>
### Linear Data Structures
|Data Structures|Handout| Code | Other Materials |
|:--------------:|:-----:|:-----:|:--------------:|
|Array|   |   |   |
|Linked List|[Singly_Linked_List](/week2/singly_linked_list.md)|[Singly Linked List.py](/week2/handout-singly%20linked%20list.py)|[Leetcode#206 Reverse Linked List](/week2/%23206%20reverse%20linked%20list.py)<br>[Leetcode#707 Design Linked List](/week2/%23707%20design%20linked%20list.py)|
|Stack|[Stack](/week3/stack%26queue.md)|[Stack.py](/week3/handout-stack.py)|[Leetcode#155 Min Stack](/week3/%23155%20min%20stack.py)|
|Queue|[Queue](/week3/stack%26queue.md#queue)|[Queue.py](/week3/handout-queue.py)|[Leetcode#232 Implementing Queue Using Stacks](/master/week3/%23232%20implement%20queue%20using%20stacks.py)<br>[Leeccode#622 Design Circular Queue](/week3/%23622%20design%20circular%20queue.py)|

### Sorting Algorithms
|Algorithms|Handout|Code|Other Materials|
|:--------:|:-----:|:--:|:-------------:|
|Bubble Sort|[Bubble Sort*](/week4/insertion%26bubble%26selection_sort.md#bubble-sort)|[Bubble_Sort.py*](/week4/handout-sorting.py)||
|Insertion Sort|[Insertion Sort*](/week4/insertion%26bubble%26selection_sort.md#insertion-sort)|[Insertion_Sort.py*](/week4/handout-sorting.py)|[Leetcode#147 Insertion Sort List](/week4/%23147%20insertion%20sort%20list.py)|
|Selection Sort|[Selection Sort*](/week4/insertion%26bubble%26selection_sort.md#Selection-sort)|[Selection_Sort.py*](/week4/handout-sorting.py)|[Time Complexities*](/week4/insertion%26bubble%26selection_sort.md#time-complexity)|
|Quick Sort|[Quick Sort](/week5/quick_sort.md)|[Quick_Sort.py](/week5/handout-quick_sort.py)|[HW1](/HW1%20Quick%20Sort)|
|Heap Sort|[Heap Data Structure & Heap Sort](/master/week6/heap%26heap_sort.md)|[Heap_Sort.py](/week6/heap_sort_04151702.py)|[Max_Heap.py](/week6/heap.py)<br>[HW2](/HW2)|
|Merge Sort|[Merge Sort](/week7/merge_sort.md)|[Merge_Sort.py](/week7/merge_sort_04151702.py)|[HW2](/HW2)|

*The descriptions of bubble sort, insertion sort, selection sort and time complexities are in the same markdown document, and thire Python codes are also in the same .py document.<br>


## Week8
### Binary Tree
- **What's Binary Tree**<br>

A binary tree is an ordered tree with the following properties:<br>
>1.Every node has at most two children.<br>
>2.Each child node is labeled as being either a ***left child*** or a ***right child***.<br>
>3.A left child preceds a right child in the order of children of a node.<br>

The subtree rooted at a left or a right child of an internal node v is called a ***left subtree*** or ***right subtree***, respectively. A binary tree is ***proper*** or ***full*** if each node has either zero or two children. A binary tree that is not proper is ***improper***.<br>

- **Properties of Binary Tree**<br>

Let T be a nonempty binary tree, and let n, n<sub>E</sub>, n<sub>I</sub>, and h denote the number of nodes, number of external nodes, number of internal nodes, and height of T, respectively(a binary tree with height h has h+1 levels). Then T has the following properties:
>1.h + 1 ≤ n ≤ 2^h+1 - 1<br>
>2.1 ≤ n<sub>E</sub> ≤ 2^h<br>
>3.h ≤ n<sub>I</sub> ≤ 2^h - 1<br>
>4.log(n+1) - 1 ≤ h ≤ n - 1<br>

If T is proper, then T has the following properties:<br>
>1.2h + 1 ≤ n ≤ 2^h+1 - 1<br>
>2.h + 1 ≤ n<sub>E</sub> ≤ 2^h<br>
>3.h ≤ n<sub>I</sub> ≤ 2^h - 1<br>
>4.log(n+1) - 1 ≤ h ≤ (n-1)/2<br>
>5.n<sub>E</sub> = n<sub>I</sub> + 1<br>

- **The Binary Tree ADT**<br>
>**`T.left(p)`**: Return the position that represents the left child of p, or None if p has no left child<br>
>**`T.right(p)`**: Return the position that represents the right child of p, or None if p has no left child<br>
>**`T.sibling(p)`**: Return the position that represents the sibling of p, or None if p has no sibling<br>

- **Some Concepts**<br>

1.**Level**: The nodes in a binary tree are organized into ***levels*** with the root node at level 0, its children at level 1, the children of level one node are at level 2, and so on.<br>
>Example: tree(a) contains 2 nodes at level 1, 4 nodes at level 2, and 2 nodes at level 3.<br>

2.**Depth**: The ***depth*** of a node is its distance from the root, with distance being the number of levels that separate the two. A node's depth corresponds to the level it occupies.<br>
>Example: in tree(a), G has a depth of 2, in tree(b) it has a depth of 3, and in (c) its depth is 6.<br>

3.**Height**: The ***height*** of a binary tree is the number of edges between the tree's root and its furthest leaf.<br>
>Example: tree(a) has a height of 3, tree(b) has a height of 5, and tree(c) has a height of 7.<br>

4**Width**: The ***width*** of a binary tree is the number of nodes on the level containing the most node.<br>
>Example: tree(a) has a width of 4, tree(b) has a width of 3, and tree(3) has a width of 1.<br>

5.**Size**: The ***size*** of a binary tree is simply the number of nodes in the tree.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week8/binary_tree1.jpg">

- **Tree Structures**<br>

1.**Full(improper) Binary Tree(完滿二元樹)**: A binary tree is a ***full binary tree*** if each node has either zero or two children, which means each interior node contains two children.
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week8/binary_tree2.jpg">

2.**Perfect Binary Tree(完美二元樹)**: A ***perfect binary tree*** is a full binary tree in which all leaf node are at the same level.
3.**Complete Binary Tree(完全二元樹)**: A binary tree of height h is a ***complete binary tree*** if it is a perfect binary tree down to height h-1 and the nodes on the lowest level fill the available slots from left to right leaving no gaps.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week8/binary_tree3.jpg">

- **Tree Traversals**<br>

1.**Preorder traversal(前序)**: In preorder traversal, we first visit the node, and then traverse the nodes in its left subtree followed by the nodes in its right subtree. Since every node is the root of its own subtree, we can repeat the same process on each node, resulting in a recursive solution.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week8/binary_tree4.jpg">

2.**Inorder traversal(中序)**: In inorder traversal, we first traverse the left subtree and then visit the node followed by the traversal of the right subtree.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week8/binary_tree5.jpg">

3.**Postorder traversal(後序)**: In a postorder traversal, the left and right subtrees of each node are traversed before the node is visited.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week8/binary_tree6.jpg">

[back to content](#content)<br>

## Week9
### Binary Search Tree(BST)
- A **binary search tree(BST)** is a binary tree in which each node contains a search key within its payload and the tree is structured such that for each interior node V:<br>
>1.All keys less than the key in node V are stored in the left subtree of V.<br>
>2.All keys greater than the key in node V are stored in the right subtree of V.<br>
- An **inorder traversal** of a binary tree visits positions in **increasing order** of their keys.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week9/BST1.jpg">

### Basic Procedures
- **Searching**: If the target value is less than the root's key, we move left and we move right if it's greater. We repeat the comparision on the root node of the subtree and take the approriate path. This process is repeated until target is located or we encounter a null child link.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week9/BST2.jpg">

- **Min/Max**: The minimum value can be located by starting at the root and following the left child links until a null link is encountered, and it means the minimum value will be found in a node that is either a leaf or an interior node with no left child. The maximum value can be found in a similar way.
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week9/BST3.jpg">

- **Insertions**: As the keys are inserted, a new node is created for each key and linked into its proper position within the tree. The new nodes are always inserted as a leaf nodes in its proper position such that the binary search tree property is maintained.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week9/BST4.jpg">

- **Successor/Predecessor**: The successor(predecessor) of a key *k* in a search tree is the smallest(largest) key that belongs to the tree and that is strictly greater than(less than) *k*.<br>

1.The idea for finding the successor of a given node *k*:<br>
>(1)If *k* has the right child, then the successor is the minimum in the right subtree of *x*.<br>
>(2)Otherwise, the successor is the parent of the farthest node that can be reached from *x* by following only right branches backward.<br>

2.The idea for finding the predecessor of a given node *k*:<br>
>(1)If *k* has the left child, then the successor is the maximum in the left subtree of *x*.<br>
>(2)Otherwise, the successor is the parent of the farthest node that can be reached from *x* by following only left branches backward.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week9/BST8.jpg">

- **Deletions**: An deletion involves searching for the node that contains the target key and then unlinking the node to remove it from the tree. When a node is removed, the remaining nodes must preserve the search tree property. Three cases should be consindered once the node has been located.<br>

1. The node *n* is a leaf: just replace *n* by null.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week9/BST5.jpg">

2. The node *n* has a single child: promote the unique child to *n*'s place.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week9/BST6.jpg">

3. The node *n* has two children:<br>
>(1)find the logical ***successor*** or ***predecessor***, *s*, of the node to be deleted, *n*<br>
>(2)copy the key from node *s* to node *n*<br>
>(3)remove node *s* from the tree<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week9/BST7.jpg">

### Time Complexities

[back to content](#content)<br>

## Week10
### Read-Black Tree
A red-black tree is a binary search tree with nodes colored rea and black in a way that satisfies the following properties:<br>
1.**Root Property**: The root is black<br>
2.**Red Property**: The children of a red node(if any) are black<br>
3.**Depth Property**: All nodes with zero or one children have the same black depth, defined as the number of black ancestors<br>

[back to content](#content)<br>

## Week11
### Hashing<br>
**Hashing** is the process of mapping a search key to a limited range of array indices with the goal of providing direct access to the keys. The keys are stored in an array called a **hash table** and a **hash function** is associated with the table. The function converts or maps the search keys to specific entries in the table.<br>
>Example: suppose we have the following set of keys: 765, 431, 96, 142, 579, 226, 903, 388 and a hash table T, containing M = 13 element. We can define a simple hash function h(·) that maps the keys to entries in the hash table: h(key) = key % M, and then we can apply the hash function to these keys, h(765) = 11, h(431) = 2, h(96) = 5, h(142) = 12, h(579) = 7...<br>

<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash1.jpg">

### Basic Procedures
- **Linear Probing**<br>

Consider what happens when we attempt to add key 226 to the hash table, the hash function maps this key to entry 5, but that entry already contains key 96.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash2.jpg">

The result is a **collision**, which occures when two or more keys map to the same hash location. If two keys map to the same table entry, we must resolve the collision by **probing** the table to find another available slot. The simpliest approach is to use a **linear probe**, which examines the table entries in sequential order starting with the first entry immediately following the original hash location. For the key value 226, the linear probe finds slots 6 available, so the key can be stored at that position.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash3.jpg">

When key 903 added, the hash function maps the key to index 6, but we just added kay 226 to this entry. The collision has to be resolved just like any other, by probing to find another slot. In the case of key 903, the linear probe leads to the slot 8.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash4.jpg">

- **Searching**<br>

Searching a hash table for a specific key is very similar to the add operation. The target key is mapped to an intial slot in the table and then it is determined if that entry contains the key. If the key is not at that location, the same probe used to add the keys to the table mustt be used to locate the target. In this case, the probe continues until the target is loacted, a null reference is encountered, or all slots have been examined. When either of the latter two situations occurs, this indicates the target key is not in the table.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash5.jpg">

- **Deletions**<br>

After finding the key, we cannot simply remove it by setting the corresponding table entry to None. Suppose we remove key 226 from our hash table and set the entry at the element 6 to None. And when we perform a search for key 903, the search function will return False, indicating the key is not in the table, even though it's located at element 8.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash6.jpg">

The reason for the unsuccessful search is due to element 6 containing a null reference from that key having been previously removed. Instead of simply setting the corresponding table entry to None, we can use a special flag to indicate the entry is now empty but it had been previously occupied. Thus, when probing to add a new key or in searching for an existing key, we know the search must continue past the slot since the target may be stored beyond this point.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash7.jpg">

### Clustering
As more keys are added to the hash table, more collisions are likely to occur. Since each collision requires a linear probe to find the next available slot, the keys begin to form **clusters**. As the clusters grow larger, so too does the probability that the next key added to the table will result in a collision.<br>
>Example: Consider the hash table in figure 11.8, what's the probability the next key will occupy the empty slot at position 4? If the next key hashes to this position, it can be stored directly into the slot without the need to probe. This also results in a probability of 1 out of 13. But the probability the next key will occupy slot 9 is 5 out of 13. If the next key hashes to any pf the slots between 5 and 9, it will be stored in slot 9 due to the linear probe required to find the first position beyond the cluster of keys. Thus, the key is five times more likel to occupy slot 9 than slot 4.<br>

This type of clustering is knowm as **primary clustering** since it occurs near the original hash position, and several different probing techniques that can be employed to reduce primary clustering.<br>
[自行整理之hash table說明，可詳閱](/HW4/hash%20table%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87%E5%8E%9F%E7%90%86%E8%A7%A3%E9%87%8B.md)

[back to content](#content)<br>

## Week12&13
