## Binary Search Tree
事實上，在對二元搜尋樹(binary search tree)進行說明前，更為嚴謹的做法是先介紹二元樹(binary tree)的概念，但因篇幅所限，故將此部分內容整理於week8的學習筆記中，若有需要可至此處詳閱[Binary tree的概念與性質](https://github.com/Xu-Yidi/fluteanzi/blob/master/README.md#week8)<br>
### Binary Search Tree
- **What's Binary Search Tree**<br>
二元搜尋樹(Binary search tree, BST)是二元樹的一種，且其每個節點(node)的值(key)滿足下列特性：值比該節點的值小的節點均在該節點的左子樹，而值比該節點的值大的節點均在該節點的右子樹<br>
- **Tree Traversals**<br>
1.**Preorder traversal(前序)**：先訪尋根節點，再訪尋左子樹，最後訪尋右子樹(中左右）<br>
2.**Inorder traversal(中序)**：先訪尋左子樹，再訪尋根節點，最後訪尋右子樹(左中右)<br>
3.**Postorder traversal(後序)**：先訪尋左子樹，再訪尋右子樹，最後訪尋根節點(左右中)<br>
4.二元搜尋樹若使用中序訪尋，得到的值將為升序排列<br>
- **Time Complexities**<br>
二元搜尋樹的時間複雜度與其樹的高度密切相關，在最差的情況下，即二元搜尋樹退化成鏈結串列(linked list)，其查找、新增和刪除的時間複雜度為O(n)，而在較佳的情況下，即二元搜尋樹較為平衡時，其查找、新增和刪除的時間複雜度為O(logn)，故保持二元搜尋樹的平衡非常重要
