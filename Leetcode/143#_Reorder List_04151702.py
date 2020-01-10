# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addNode(self, node):
        self.tail.next = node
        self.tail = node
    
    '''
    def getElement(self, node):
        result = []
        curNode = node
        while curNode is not None:
            result.append(curNode.val)
            curNode = curNode.next
        print(result)        
    '''
    
    def reorderList(self, head):
        self.__init__()
        
        if head is None or head.next is None:
            return        
            
        stack = []
        
        curNode = head
        while curNode is not None:
            stack.append(curNode.val)
            curNode = curNode.next
        
        index = 0
        
        self.head = ListNode(stack[0])
        self.tail = self.head
        
        
        while index <= (len(stack)+1)//2 - 1:
            self.addNode(ListNode(stack[len(stack)-1-index]))
            
            if len(stack) % 2 == 0:
                if index == (len(stack)+1)//2 - 1:
                    break
            
            index+=1
            
            self.addNode(ListNode(stack[index]))
            
            if len(stack) % 2 == 1:
                if index == (len(stack)+1)//2 - 1:
                    break                
        
        head.next = self.head.next
        #self.getElement(head)
        
