# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        
        if current == None:
            return current
        if current.next == None:
            return current
        
        temp = self.reverseList(current.next)
        
        current.next.next = current
        current.next = None
        
        return temp