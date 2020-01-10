# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return
        
        length = 0
        curNode = head
        while curNode is not None:
            length += 1
            curNode = curNode.next
        mid_index = (length+2)//2
        
        for i in range(mid_index-1):
            head = head.next
        return head
        
