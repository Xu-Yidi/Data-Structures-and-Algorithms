# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:        
        if head is None:
            return 
        
        curNode = head
        if curNode.next is None:
            return curNode
        
        while curNode is not None and curNode.next is not None:
            tempVal = curNode.val
            curNode.val = curNode.next.val
            curNode.next.val = tempVal
            curNode = curNode.next.next
        return head
