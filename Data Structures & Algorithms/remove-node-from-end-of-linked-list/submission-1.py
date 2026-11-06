# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_node_index = 0
        current_head = head
        previous_head = None

        list_length = 0
        list_head_length = head
        while list_head_length != None:
            list_head_length = list_head_length.next
            list_length += 1

        while current_head != None:
            if current_node_index == (list_length - n): # if this is the node to remove
                if previous_head == None: # if the node is the first node
                    return current_head.next
                previous_head.next = current_head.next

            current_node_index += 1
            previous_head = current_head
            current_head = current_head.next
        return head
        