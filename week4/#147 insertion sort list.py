# Definition for singly-linked list.
#class ListNode:
    #def __init__(self, x):
    #self.val = x
    #self.next = None
    
class Solution:
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        cur = head
        
        while cur and cur.next:
            if cur.next.val >= cur.val:
                cur = cur.next
            else:
                pre = dummyNode
                insertNode = cur.next
                dummyNext = insertNode.next
                while pre.next is not None and pre.next.val <= insertNode.val:
                    pre = pre.next
                preNext = pre.next
                cur.next = dummyNext
                pre.next = insertNode
                insertNode.next = preNext
        
        return dummyNode.next
                       
