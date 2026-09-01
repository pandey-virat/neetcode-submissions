# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow  = None
        while head is not None:
            fast = head.next
            head.next = slow
            slow = head
            head = fast
        return slow
        


        