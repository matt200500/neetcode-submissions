# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_current_head = list1
        list2_current_head = list2
        starting_head = None

        # initialize starting head of linked list to return
        if list1_current_head != None and list2_current_head != None:
            if list1_current_head.val <= list2_current_head.val:
                starting_head = list1_current_head
                list1_current_head = list1_current_head.next
            else:
                starting_head = list2_current_head
                list2_current_head = list2_current_head.next
        elif list1_current_head != None: # if first head not null
            starting_head = list1_current_head
            list1_current_head = list1_current_head.next
        elif list2_current_head != None: # if second head not null
            starting_head = list2_current_head
            list2_current_head = list2_current_head.next
        else: # if both null
            return None

        current_head = starting_head

        # loop through and combine linked lists
        while list1_current_head != None and list2_current_head != None:
            if list1_current_head.val <= list2_current_head.val:
                current_head.next = list1_current_head
                current_head = list1_current_head
                list1_current_head = list1_current_head.next
            else:
                current_head.next = list2_current_head
                current_head = list2_current_head
                list2_current_head = list2_current_head.next
        
        while list1_current_head != None:
            current_head.next = list1_current_head
            current_head = list1_current_head
            list1_current_head = list1_current_head.next

        while list2_current_head != None:
            current_head.next = list2_current_head
            current_head = list2_current_head
            list2_current_head = list2_current_head.next

        return starting_head