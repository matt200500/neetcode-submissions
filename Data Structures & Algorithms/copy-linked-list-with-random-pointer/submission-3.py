"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current_head = head

        if head == None:
            return None
        
        node_mapping = {}
        while current_head != None: 
            new_node = Node(current_head.val)
            node_mapping[current_head] = new_node
            current_head = current_head.next
        
        for original_node, new_node in node_mapping.items():

            # for setting the .next of the new node
            if original_node.next != None:
                next_node = node_mapping[original_node.next]
                new_node.next = next_node
            else:
                new_node.next = None
            
            # for setting the .random of the new node
            if original_node.random != None:
                random_node = node_mapping[original_node.random]
                new_node.random = random_node
            else:
                new_node.random = None
        
        return node_mapping[head]
            



        