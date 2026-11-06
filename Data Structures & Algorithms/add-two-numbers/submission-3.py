# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_number = 0
        second_number = 0

        current_head = l1
        current_power = 1
        while current_head != None:
            first_number += (current_head.val * current_power)
            current_power = current_power * 10
            current_head = current_head.next

        current_head = l2
        current_power = 1
        while current_head != None:
            second_number += (current_head.val * current_power)
            current_power = current_power * 10
            current_head = current_head.next

        final_number = str(first_number + second_number)
        initial_head = ListNode()
        current_head = initial_head
        previous_head = None
        for character in final_number[::-1]:
            current_head.val = int(character)
            next_head = ListNode()
            current_head.next = next_head
            previous_head = current_head
            current_head = current_head.next
        previous_head.next = None

        return initial_head
        
        