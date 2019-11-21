## Binary Search Tree
### Insert
Insert(插入)：在原本的binary search tree中插入新的節點，小於等於則向左走，大於則向右走，直至新節點確定正確位置<br>
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

 
