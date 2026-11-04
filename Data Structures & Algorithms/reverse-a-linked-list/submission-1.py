# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_head = None
        current_head = head
        while current_head != None:
            next_head = current_head.next
            current_head.next = previous_head
            previous_head = current_head
            current_head = next_head
            

        return previous_head


        
        