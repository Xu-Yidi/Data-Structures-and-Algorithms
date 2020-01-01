## Binary Tree
### What's Binary Tree**<br>

A binary tree is an ordered tree with the following properties:<br>
>1.Every node has at most two children.<br>
>2.Each child node is labeled as being either a ***left child*** or a ***right child***.<br>
>3.A left child preceds a right child in the order of children of a node.<br>

The subtree rooted at a left or a right child of an internal node v is called a ***left subtree*** or ***right subtree***, respectively. A binary tree is ***proper*** or ***full*** if each node has either zero or two children. A binary tree that is not proper is ***improper***.<br>

### Properties of Binary Tree**<br>

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

### The Binary Tree ADT**<br>
>**`T.left(p)`**: Return the position that represents the left child of p, or None if p has no left child<br>
>**`T.right(p)`**: Return the position that represents the right child of p, or None if p has no left child<br>
>**`T.sibling(p)`**: Return the position that represents the sibling of p, or None if p has no sibling<br>

### Some Concepts**<br>

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

### Tree Structures**<br>

1.**Full(improper) Binary Tree(完滿二元樹)**: A binary tree is a ***full binary tree*** if each node has either zero or two children, which means each interior node contains two children.
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week8/binary_tree2.jpg">

2.**Perfect Binary Tree(完美二元樹)**: A ***perfect binary tree*** is a full binary tree in which all leaf node are at the same level.
3.**Complete Binary Tree(完全二元樹)**: A binary tree of height h is a ***complete binary tree*** if it is a perfect binary tree down to height h-1 and the nodes on the lowest level fill the available slots from left to right leaving no gaps.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week8/binary_tree3.jpg">

### Tree Traversals**<br>

1.**Preorder traversal(前序)**: In preorder traversal, we first visit the node, and then traverse the nodes in its left subtree followed by the nodes in its right subtree. Since every node is the root of its own subtree, we can repeat the same process on each node, resulting in a recursive solution.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week8/binary_tree4.jpg">

2.**Inorder traversal(中序)**: In inorder traversal, we first traverse the left subtree and then visit the node followed by the traversal of the right subtree.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week8/binary_tree5.jpg">

3.**Postorder traversal(後序)**: In a postorder traversal, the left and right subtrees of each node are traversed before the node is visited.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week8/binary_tree6.jpg">
