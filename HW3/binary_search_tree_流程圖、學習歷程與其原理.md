## Binary Search Tree
事實上，在對二元搜尋樹(binary search tree)進行說明前，更為嚴謹的做法是先介紹二元樹(binary tree)的概念，但因篇幅所限，故將此部分內容整理於week8的學習筆記中，若有需要可至此處詳閱[Binary tree的概念、性質與訪尋](https://github.com/Xu-Yidi/fluteanzi/blob/master/README.md#week8)<br>
### Binary Search Tree
- **What's Binary Search Tree**<br>

二元搜尋樹(Binary search tree, BST)是二元樹的一種，且其每個節點(node)的值(key)滿足下列特性：值比該節點的值小的節點均在該節點的左子樹，而值比該節點的值大的節點均在該節點的右子樹<br>
- **Tree Traversals**<br>

1.**Preorder traversal(前序)**：先訪尋根節點，再訪尋左子樹，最後訪尋右子樹(中左右）<br>
2.**Inorder traversal(中序)**：先訪尋左子樹，再訪尋根節點，最後訪尋右子樹(左中右)<br>
3.**Postorder traversal(後序)**：先訪尋左子樹，再訪尋右子樹，最後訪尋根節點(左右中)<br>
4.二元搜尋樹若使用中序訪尋，得到的值將為升序排列<br>
- **Basic Procedures**<br>

1.**Insert(新增)**：不斷將二元搜尋樹上的節點值與欲新增之值比較，小於等於則向左邊走，大於則向右邊走，直至確定其位置<br>
2.**Delete(刪除)**：刪除分為三種情況
>(a)欲刪除的節點為葉節點：直接刪除即可<br>
>(b)欲刪除的節點有一個子節點：直接將其唯一之子節點接在其父節點上<br>
>(c)欲刪除的節點有兩個子節點：找到欲刪除節點的後繼節點(successor)，將其值替換為後繼節點的值，並刪除後繼節點，而後繼節點為為葉節點或只有右子節點，故為(a)(b)情況<br>

3.**Search(查詢)**：不斷將二運搜尋樹的節點值與目標值進行比較，小於等於則向左走，大於則向右走，直至查詢到該節點或節點不存在<br>
4.**Modify(修改)**:將具有某個目標值的節點的值修改為新的給定值，需仍保持二元搜尋樹的性質且樹高小於等於原來的樹高。作業中的想法為先使用前序訪尋得到全部節點的值，修改目標值並進行排序，再使用反復抽取中位數的方法確定其插入順序，如果此法不能使樹高小於等於原先樹高，則會隨機抽取25組不同的插入順序，並返回其中樹高最小的情況<br>

- **Time Complexities**<br>
二元搜尋樹的時間複雜度與其樹的高度密切相關，在最差的情況下，即二元搜尋樹退化成鏈結串列(linked list)時，其查找、新增和刪除的時間複雜度為O(n)，而在較佳的情況下，即二元搜尋樹較為平衡時，其查找、新增和刪除的時間複雜度為O(logn)，故保持二元搜尋樹的平衡非常重要

### Flowchart
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week9/binary_search_tree.jpg">

### 學習歷程
此次作業難度較之前有大幅增加，雖然已經花費了相當的精力與時間，但仍然感覺自己撰寫的程式有許多疏漏之處，尤其是delete部分，倘若不反復嘗試不同的測值極易忽略某些特殊情況，但無論如何，在撰寫程式與不斷試錯的過程也是能力提升的過程。因為程式的詳細說明已呈現在binary_search_tree_新增、刪除、查詢、修改功能說明的文檔中，此處想對作業中遇到的錯誤進行回顧與總結<br>

1.若需要回傳內容，遞迴函數前也要加return，在寫程式的過程中一度忘記加return，發現print()可以得到正確內容卻無法回傳內容，除錯很久才發現是沒有在遞迴前加return<br>
```Python
    def search(self, root, target):       
        if target == root.val:                #如果目標值與root的值一致，則回傳root節點  
            return root
        else:
            if target < root.val:             #如果目標值比root的值小
                if root.left is not None:     #如果root有左子節點，則繼續向左走
                    root = root.left
                else:                         #如果root沒有左子節點，則說明無法找到具有該目標值的節點，故回傳None
                    return None
            
            if target > root.val:             #如果目標值比root的值大
                if root.right is not None:    #如果root有右子節點，則繼續向右走
                    root = root.right
                else:
                    return None               #否則無法找到具有該目標的節點，並回傳None      
        return self.search(root, target)      #遞迴地呼叫search使與目標值比較的root不斷向右或向左走，直至找到具有目標值的節點或回傳Non
```
2.當list中元素的排列組合非常多，列出全部的排列組合在進行隨機抽取非常浪費時間，可採取直接對該list進行亂序的方法。原本想用itertools.permutations()得到所有的排列組合，但實際執行時元素數目較多時筆電極易陷入故障，而採取random.shuffle()直接進行亂序以代替抽樣是非常巧妙的解決辦法

```Python
            for i in range(25):                   #隨機抽取25組排列組合     
                random.shuffle(insert_element)    #對根節點之外的節點之插入順訊進行亂序
                #print(insert_element)                
                insert_order.append(insert_element)            
                root = TreeNode(new_tree_element[0]) 
                for item in insert_element:
                    self.insert(root, item)
                tree_height_try.append(self.getHeight(root))
```
3.熟練使用continue,break,pass非常重要，此次作業在delete的部分用了較多的條件判斷，能否在正確位置使用continue關乎程式能否正確執行，例如在delete函數中若符合一種情況並執行相應的分函數後，應使用continue跳出本次循環
```Python
    def delete(self, root, target):
        #因為search只能尋找到具有指定值的第一個節點，故當無法再尋找到具有指定值的節點時，刪除完畢
        while self.search(root, target) is not None:      #檢查欲刪除的節點是否為根節點     
            if self.father(root, self.search(root, target)) is None:
                self.delete_5(root, target)
            else:
                if self.search(root, target).left is None and self.search(root, target).right is None:
                    self.delete_1(root, target)
                    continue                              #執行相應的delete分函數後，跳出此次循環
                if self.search(root, target).left is not None and self.search(root, target).right is None:
                    self.delete_2(root, target)
                    continue
                if self.search(root, target).left is None and self.search(root, target).right is not None:
                    self.delete_3(root, target)
                    continue
                if self.search(root, target).left is not None and self.search(root, target).right is not None:
                    self.delete_4(root, target)
                    continue
        return root    
```
4.正確撰寫遞迴的關鍵之一在於停止條件的設立，如果使用遞迴而沒有設置停止條件，則會陷入無窮迴圈，為在練習時防止此種情況，可在程式前方加上
```Python
import sys
sys.getrecursionlimit()
```
### Reference
Michael T. Goodrich & Roberto Tamassia &Michael H. Goldwasser. *Data Structures and Algorithms in Python*.(CH11 Search Trees/ Section11.1 Binary Search Tree/ Page460-465)<br>
Binary Search Tree: Intro(簡介) http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html
