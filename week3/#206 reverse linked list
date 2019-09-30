# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        preNode = None
        curNode = head
        while curNode is not None:
            next = curNode.next
            curNode.next = preNode
            preNode = curNode
            curNode = next
        head = preNode
        return head

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:        
        if head is None or head.next is None:
            return head
        else:
            preNode = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return preNode
        
