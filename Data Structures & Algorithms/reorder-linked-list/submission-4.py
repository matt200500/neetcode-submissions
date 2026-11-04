# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        previous_slow_head = None
        slow_head = head
        fast_head = head

        # get middle
        while fast_head != None and fast_head.next != None:
            previous_slow_head = slow_head
            slow_head = slow_head.next
            fast_head = fast_head.next.next

        if previous_slow_head == None:
            return
        previous_slow_head.next = None # cut off left list from right

        # reverse right list
        previous_head = None
        current_head = slow_head
        while current_head != None:
            next_head = current_head.next
            current_head.next = previous_head
            previous_head = current_head
            current_head = next_head

        right_list_start = previous_head
        left_list_start = head
        current_list = ListNode()
        starting_index = current_list
        side_index = True # True means left side and False means right side

        while left_list_start != None and right_list_start != None:
            if side_index: # if we are adding left side head
                current_list.next = left_list_start
                left_list_start = left_list_start.next
                side_index = False
            else: # if we are adding right side head
                current_list.next = right_list_start
                right_list_start = right_list_start.next
                side_index = True
            current_list = current_list.next

        if left_list_start != None:
            current_list.next = left_list_start
        elif right_list_start != None:
            current_list.next = right_list_start

        head = starting_index.next

        