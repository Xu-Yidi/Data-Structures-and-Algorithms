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
