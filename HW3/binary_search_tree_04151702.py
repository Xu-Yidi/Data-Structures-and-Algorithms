# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:32:14 2019

@author: Yidi
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):    
    def __init__(self):
        self.content = list()
        self.element_order = list()    
        
    def insert(self, root, value):
        newNode = TreeNode(value)
        if value <= root.val:
            if root.left is not None:
                root = root.left            
            else:
                root.left = newNode
                return root.left
        
        if value > root.val:
            if root.right is not None:
                root = root.right
            else:
                root.right = newNode
                return root.right
        return self.insert(root, value) 

    def delete(self, root, target):
        while self.search(root, target) is not None:
            #print(root.val)
            if self.father(root, self.search(root, target)) is None:
                root = self.delete_5(root, target)
                if root is None:
                    return
            else:
                if self.search(root, target).left is None and self.search(root, target).right is None:
                    self.delete_1(root, target)
                    continue
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

    def search(self, root, target):       
        if target == root.val:        
            return root
        else:
            if target < root.val:
                if root.left is not None:
                    root = root.left
                else:
                    return None
            
            if target > root.val:
                if root.right is not None:
                    root = root.right
                else:
                    return None                    
        return self.search(root, target)    
        
    def modify(self, root, target, new_val):            
        tree_height = self.getHeight(root)          
        new_tree_element = self.order_element(self.change_element(root, target, new_val))
        root = TreeNode(new_tree_element[0])               
        for i in range(1, len(new_tree_element)):
            self.insert(root, new_tree_element[i])
        new_tree_height = self.getHeight(root)        
        if new_tree_height <= tree_height:
            #print("yes")
            return root
        else:      
            insert_element = new_tree_element[1:]                    
            tree_height_try = []            
            insert_order_try = []                    
            
            import random                    
            for i in range(25):            
                insert_order = random.sample(insert_element, len(insert_element))           
                insert_order_try.append(insert_order)                        
                root = TreeNode(new_tree_element[0]) 
                for item in insert_order:
                    self.insert(root, item)
                tree_height_try.append(self.getHeight(root))
            min_index = tree_height_try.index(min(tree_height_try))
            root = TreeNode(new_tree_element[0])
            for item in insert_order_try[min_index]:
                self.insert(root, item)
            return root    
        
    def preorderTraversal(self, node):
        self.content.append(node.val)
        if node.left is not None:
            self.preorderTraversal(node.left)
      
        if node.right is not None:
            self.preorderTraversal(node.right)
        else:
            return 
        
    def preorderTraversal_1(self, node):
        print(node.val)
        if node.left is not None:
            self.preorderTraversal_1(node.left)
      
        if node.right is not None:
            self.preorderTraversal_1(node.right)
        else:
            return 

    def father(self, root, node):
        if node == root:
            return None
        
        if node.val <= root.val:

            if root.left is not None:
                if root.left == node:
                    return root
                else:
                    root = root.left
            else:
                return
        
        if node.val > root.val:

            if root.right is not None:
                if root.right == node:
                    return root
                else:
                    root = root.right
            else:
                return
                    
        return self.father(root, node)        

    def successor(self, node):  
        if node.left is not None:
            node = node.left
        else:
            return node
        return self.successor(node)

    def delete_1(self, root, target):
        #if self.search(root, target).left is None and self.search(root, target).right is None:
        if self.father(root, self.search(root, target)).val >= target: 
            self.father(root, self.search(root, target)).left = None
            return 
        if self.father(root, self.search(root, target)).val < target:  
            self.father(root, self.search(root, target)).right = None
            return    
           
    def delete_2(self, root, target): 
        #if self.search(root, target).left is not None and self.search(root, target).right is None:
        tempNode = self.search(root, target).left
        if self.father(root, self.search(root, target)).val >= target:
            self.father(root, self.search(root, target)).left = tempNode
            return 
        if self.father(root, self.search(root, target)).val < target:
            self.father(root, self.search(root, target)).right = tempNode
            return 
        
    def delete_3(self, root, target):
        #if self.search(root, target).left is None and self.search(root, target).right is not None:
        tempNode = self.search(root, target).right
        if self.father(root, self.search(root, target)).val >= target:            
            self.father(root, self.search(root, target)).left = tempNode
            return 
        if self.father(root, self.search(root, target)).val < target:
            self.father(root, self.search(root, target)).right = tempNode
            return 

    def delete_4(self, root, target):
        #if self.search(root, target).left is not None and self.search(root, target).right is not None:
        tempNode_1 = self.search(root, target)
        tempNode_2 = self.successor(self.search(root, target).right)
               
        if tempNode_2.left is None and tempNode_2.right is None:
            if self.father(root, tempNode_2).val >= tempNode_2.val:
                self.father(root, tempNode_2).left = None
            else:
                self.father(root, tempNode_2).right = None
            
            if self.father(root, tempNode_1).val >= target:           
                self.father(root, tempNode_1).left.val = tempNode_2.val
                return           
            if self.father(root, tempNode_1).val < target:
                self.father(root, tempNode_1).right.val = tempNode_2.val
                return        
        
        if tempNode_2.left is None and tempNode_2.right is not None:
            if self.father(root, tempNode_2).val >= tempNode_2.val:
                self.father(root, tempNode_2).left = tempNode_2.right
            else: 
                self.father(root, tempNode_2).right = tempNode_2.right
            
            if self.father(root, tempNode_1).val >= target:           
                self.father(root, tempNode_1).left.val = tempNode_2.val
                return           
            if self.father(root, tempNode_1).val < target:
                self.father(root, tempNode_1).right.val = tempNode_2.val
                return 
     
    def delete_5(self, root, target):        
        if self.search(root, target).left is None and self.search(root, target).right is None:
            root = None
            return root 
            
        if self.search(root, target).left is not None and self.search(root, target).right is None:
            root = root.left
            return root
        
        if self.search(root, target).left is None and self.search(root, target).right is not None:
            root = root.right
            return root
        
        if self.search(root, target).left is not None and self.search(root, target).right is not None:
            tempNode = self.successor(self.search(root, target).right)   
            if tempNode.left is None and tempNode.right is None:
                if self.father(root, tempNode).val >= tempNode.val:
                    self.father(root, tempNode).left = None
                else:
                    self.father(root, tempNode).right = None                    
                root.val = tempNode.val
                return root         
                                   
            if tempNode.left is None and tempNode.right is not None:
                if self.father(root, tempNode).val >= tempNode.val:
                    self.father(root, tempNode).left = tempNode.right
                else:   
                    self.father(root, tempNode).right = tempNode.right
                root.val = tempNode.val
                return root

    def getHeight(self, root):        
        if root is None:
            return -1
        else:
            left_height = self.getHeight(root.left)
            right_height = self.getHeight(root.right)
            return max(left_height, right_height) + 1
    
    def change_element(self, root, target, new_val):
        self.__init__()
        self.preorderTraversal(root)
        tree_element = self.content
        for i in range(0, len(tree_element)):
            if tree_element[i] == target:
                tree_element[i] = new_val
        tree_element = sorted(tree_element)
        return tree_element
    
    def order_element(self, seq):
        if len(seq) <= 0:
            return   
        self.element_order.append(seq[int(len(seq)/2)])
        left = seq[:int(len(seq)/2)]  
        right = seq[int(len(seq)/2)+1:]
        
        self.order_element(left)
        self.order_element(right)
        
        return self.element_order  


#概念理解參照課本 Michael T. Goodrich & Roberto Tamassia &Michael H. Goldwasser. 
#Data Structures and Algorithms in Python.(CH11 Search Trees/ Section11.1 Binary Search Tree/ Page460-465)
#程式為自行撰寫，無其他參考資料
