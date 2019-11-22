## Binary Search Tree
新增、刪除、查詢、修改的概念以及流程圖以呈現在binary_search_tree_流程圖、學歷歷程與原理的檔案中，故在此不再重複敘述，本檔案主要對四個功能的程式進行說明
### Insert
Insert(新增)：在原本的binary search tree中插入新的節點，小於等於則向左走，大於則向右走，直至新節點確定正確位置<br>
```Python
class Solution(object):    
    def __init__(self):
        self.content = list()
        self.element_order = list()    
        
    def insert(self, root, value):
        newNode = TreeNode(value)      #生成一個新的節點
        if value <= root.val:          #如果新節點的值小於等於root的值
            if root.left is not None:  #如果root有左子節點，則繼續向左邊走
                root = root.left            
            else:
                root.left = newNode    #如果root沒有左子節點，則將此新節點作為其左子節點
                return root.left       #若已經確定新節點的位置，則返回
        
        if value > root.val:           #如果新節點的值大於root的值
            if root.right is not None: #如果root有右子節點，則繼續向右走
                root = root.right
            else:
                root.right = newNode   #如果root沒有右子節點，則將此新節點作為其右子節點
                return root.right
        return self.insert(root, value) #遞迴地呼叫insert使與新節點比較的root不斷向左走或向右走，直至確定新節點的位置
 ```
### Delete
Delete(刪除)：在原本的binary search tree中刪除具特定值的所有節點，刪除一般分為三種情況：<br>
1.欲刪除的節點沒有子節點，即其為葉節點，則直接刪除即可<br>
```Python
    def delete_1(self, root, target):
        #if self.search(root, target).left is None and self.search(root, target).right is None:
        if self.father(root, self.search(root, target)).val >= target:  #若其父節點的值比該欲刪除的節點值大
            self.father(root, self.search(root, target)).left = None    #則將其父節點的左子節點指定為空
            return                                                      #刪除完則返回
        if self.father(root, self.search(root, target)).val < target:   #若其父節點的值比該欲刪除的節點值小
            self.father(root, self.search(root, target)).right = None   #則將其父節點的右子節點指定為空
            return    
```
2.欲刪除的節點具有左子節點或右子節點，則將其子節點直接接在其父節點上，以下的代碼將其分為只有左子節點與只有右子節點兩種情況<br>
```Python
    #欲刪除的節點有左子節點但無右子節點    
    def delete_2(self, root, target): 
        #if self.search(root, target).left is not None and self.search(root, target).right is None:
        tempNode = self.search(root, target).left                        #使用tempNode暫存欲刪除節點的左子節點
        if self.father(root, self.search(root, target)).val >= target:   #若其父節點的值比該欲刪除的節點值大
            self.father(root, self.search(root, target)).left = tempNode #則將其父節點的左子節點指定為該與刪除節點的左子節點
            return 
        if self.father(root, self.search(root, target)).val < target:    #若其父節點的值比該欲刪除的節點值小
            self.father(root, self.search(root, target)).right = tempNode#則將其父節點的右子節點指定為該欲刪除節點的左子節點
            return 
    
    #欲刪除的節點有右子節點但無左子節點   
    def delete_3(self, root, target):
        #if self.search(root, target).left is None and self.search(root, target).right is not None:
        tempNode = self.search(root, target).right                       #使用tempNode暫存欲刪除節點的右子節點
        if self.father(root, self.search(root, target)).val >= target:   #若其父節點的值比該欲刪除的節點值大        
            self.father(root, self.search(root, target)).left = tempNode #則將其父節點的左子節點指定為該欲刪除節點的右子節點
            return 
        if self.father(root, self.search(root, target)).val < target:    #若其父節點的值比該欲刪除的節點值小
            self.father(root, self.search(root, target)).right = tempNode#則將其父節點的右子節點指定為該欲刪除節點的右子節點
            return 
```
3.欲刪除的節點同時具有左子節點與右子節點，則需要先找到該欲刪除節點successor(即為比其大的所有節點中最小的)，並將此successor的值替換欲刪除節點的值，再將successor刪除，值得注意的是，successor只可能為葉節點或只有右子節點，故可用上述兩種方法進行刪除
```Python
    #欲刪除的節點同時具有左子節點與右子節點
    def delete_4(self, root, target):
        #if self.search(root, target).left is not None and self.search(root, target).right is not None:
        tempNode_1 = self.search(root, target)                           #使用tempNode_1暫存該欲刪除節點
        tempNode_2 = self.successor(self.search(root, target).right)     #使用tempNode_2暫存欲刪除節點的successor
               
        if tempNode_2.left is None and tempNode_2.right is None:         #若successor為葉節點
            if self.father(root, tempNode_2).val >= tempNode_2.val:      #刪除successor，即為delete_1之情形
                self.father(root, tempNode_2).left = None
            else:# self.father(root, tempNode_2).val < tempNode_2.val:
                self.father(root, tempNode_2).right = None
            
            if self.father(root, tempNode_1).val >= target:              #若其父節點的值比該欲刪除的節點大
                self.father(root, tempNode_1).left.val = tempNode_2.val  #則將其父節點的左子節點(其實即為該欲刪除的節點)的值賦值為successor的值
                return           
            if self.father(root, tempNode_1).val < target:               #若其父節點的值比該欲刪除的節點小
                self.father(root, tempNode_1).right.val = tempNode_2.val #則將其父節點的右子節點(其實即為該欲刪除的節點)的值賦值為successor的值
                return        
        
        if tempNode_2.left is None and tempNode_2.right is not None:     #若successor只有右子節點
            if self.father(root, tempNode_2).val >= tempNode_2.val:      #刪除successor, 即為delete_3之情形
                self.father(root, tempNode_2).left = tempNode_2.right
            else: #self.father(root, tempNode_2).val < tempNode_2.val:
                self.father(root, tempNode_2).right = tempNode_2.right 
            
            if self.father(root, tempNode_1).val > target:               #將succesor的值替代該欲刪除的節點的值，原理同上
                self.father(root, tempNode_1).left.val = tempNode_2.val
                return           
            if self.father(root, tempNode_1).val < target:
                self.father(root, tempNode_1).right.val = tempNode_2.val
                return 
```
下面的程式片段為delete函數的主函數，為分別判斷欲刪除的節點屬於何種狀況並分別執行對應狀況下的delete分函數，當欲刪除的節點為根節點時，情況略有不同，但其原理仍然為三種狀況。值得注意的是，當找到對應的狀況並執行完相應的delete分函數時，應使用continue跳出此次循環，否則會產生錯誤
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
 
 ### Search
 Search(查詢)：返回具有欲查找的值的第一個節點，即從根節點開始不斷與目標值比較大小，目標值較小則向左走，目標值較大則向右走
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
        return self.search(root, target)      #遞迴地呼叫search使與目標值比較的root不斷向右或向左走，直至找到具有目標值的節點或回傳None
```

### Modify
Modify(修改)：將所有具有某個目標值的節點的值修改成另一給定的值，且修改完成後需保持binary reseach tree的形態，並使樹高小於等於原來的樹高。嚴格意義上，使樹高均衡的方法應該是採用AVLtree或是red black tree，但因為時間不充裕之故，作業中將使用反復抽取中位數的方法來盡量使所建的樹保持均衡，其主要做法為先訪尋所有的節點，對目標值進行修改，將所有的值進行排序後再不斷抽取中位數以決定insert的順序。舉例而言，修改並排序後的所有值為[17,24,26,63,65,89,93]，則root應為中位數63，第二個插入的節點為[17,24,26]的中位數24，第三個插入的節點為[65,89,93]的中位數89，以此類推，得到所有節點insert的順序為[63,24,89,17,26,65,93]。如果通過反復抽取中位數仍無法使樹高小於等於原本的樹高，則將採用隨機抽取的方法，隨機抽取25組具有[63,24,89,17,26,65,93]的值的排列組合（根節點固定），如[63,17,26,65,24,93,89]，即隨機決定除了根節點外的insert的順序，並返回25組中樹高最小的情況
```Python
    def modify(self, root, target, new_val):
        tree_height = self.getHeight(root)    #得到modify前樹的高度      
        #print("tree_height:" + str(tree_height))        
        #排序後且進行反復抽取中位數後得到的節點插入順序
        new_tree_element = self.order_element(self.change_element(root, target, new_val))
        #print(new_tree_element)
        root = TreeNode(new_tree_element[0])       #將第一個插入的值視為root        
        for i in range(1, len(new_tree_element)):  #依序插入其餘節點
            self.insert(root, new_tree_element[i])
        new_tree_height = self.getHeight(root)     #得到modify後樹的高度
        #print("new_tree_height:" + str(new_tree_height))        
        if new_tree_height <= tree_height:         #如果modify後樹的高度比modify前樹的高度小，返回新建的樹即可
            #print("yes")
            return root
        else:                                      #否則將採取隨機抽取的方法
            #new_tree_element = self.order_element(self.change_element(root, target, new_val))      
            insert_element = new_tree_element[1:]  #根節點固定，故insert順序只考慮根節點之外的值                
            tree_height_try = []            
            insert_order = []                 
            import random           
            for i in range(25):                   #隨機抽取25組排列組合     
                random.shuffle(insert_element)    #對根節點之外的節點之插入順訊進行亂序
                #print(insert_element)                
                insert_order.append(insert_element)            
                root = TreeNode(new_tree_element[0]) 
                for item in insert_element:
                    self.insert(root, item)
                tree_height_try.append(self.getHeight(root))
            #print(tree_height_try)
            min_index = tree_height_try.index(min(tree_height_try)) #找出25組排列組合中樹高最小的狀況
            root = TreeNode(new_tree_element[0])
            #print(insert_order[min_index])
            for item in insert_order[min_index]:
                self.insert(root, item)
            return root    
```
### Reference
Michael T. Goodrich & Roberto Tamassia &Michael H. Goldwasser. *Data Structures and Algorithms in Python*.(CH11 Search Trees/ Section11.1 Binary Search Tree/ Page460-465)<br>
Rance D. Necaise.*Data Structures and Algorithms using Python*.(CH14 Search Trees/ Section14.1 Binary Search Tree/ Page412-425)<br>
注：概念參考課本，程式為自行撰寫
