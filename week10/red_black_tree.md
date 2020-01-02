## Red-Black Tree
A red-black tree is a binary search tree with nodes colored rea and black in a way that satisfies the following properties:<br>
1.**Root Property**: The root is black<br>
2.**Red Property**: The children of a red node(if any) are black<br>
3.**Depth Property**: For each node, all path from the node to descendant leaves contains the same number of black nodes.<br>

### Insertions
step1: 在紅黑樹中新增節點時，會先將欲新增的節點設為紅色(新增的節點為root除外)，插入節點之方法與BST相同;<br>
step2: 若新增的節點接在黑色節點後，則仍滿足紅黑樹的性質，若新增的節點接在紅色節點後(double red problem)，則需要進行調整:<br>
- **Case 1: parent node與uncle node皆為紅色**<br>
(1)將欲插入節點的parent node與uncle node塗成黑色;<br>
(2)將其parent node的parent node(即其grandparent node)塗成紅色;<br>
(3)判斷是否需要繼續對grandparent node進行調整，如果grandparent node的parent node也為紅色，則需重複上述過程<br  >
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week10/RBT_insertion1.jpg">

- **Case 2: parent node為紅色，uncle node為黑色(or Nil)，且欲插入之節點為其parent node的left child**<br>
(1)對欲插入節點的grandparent node進行向右旋轉(right rotation);<br>
(2)交換旋轉後其parent node與新生成的sibling node的顏色;<br>
上述假設欲插入節點之parent node為其grandparent node的left child，其對稱情況為parent node為grandparent node的right child，欲插入節點為parent node的right child，此時需對grandparent node進行向左旋轉，其餘步驟相同<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week10/RBT_insertion2.jpg">

- **Case 3: parent node為紅色，uncle node為黑色(or Nil)，且欲插入之節點為其parent node的right child**<br>
(1)對欲插入節點之parent node進行向左旋轉(left rotation);<br>
(2)對旋轉後的parent node(旋轉後已成為left child)進行Case 2中之操作;<br>
上述同樣假設欲插入節點的parent node為其grandparent node的left child，其對稱情況為parent node為grandparent node的right child，欲插入節點為parent node的left child，此時需對parent node進行向右旋轉，再回到Case 2中的對稱情況<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week10/RBT_insertion3.png">
