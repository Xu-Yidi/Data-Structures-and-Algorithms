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




>3.欲刪除的節點同時具有左子節點與右子節點
 
 
