# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_head = head
        fast_head = head
        while fast_head != None:

            if fast_head.next == None:
                return False
            
            fast_head = fast_head.next.next
            slow_head = slow_head.next

            if slow_head == fast_head:
                return True

        return False



        