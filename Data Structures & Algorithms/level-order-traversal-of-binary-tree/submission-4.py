# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        queue = deque()
        if root == None:
            return output
            
        queue.append((root,0))
        while len(queue) != 0:
            popped_element = queue.popleft()
            if len(output) <= popped_element[1]:
                output.append([])
            output[popped_element[1]].append(popped_element[0].val)

            if popped_element[0].left != None:
                queue.append((popped_element[0].left,popped_element[1]+1))
            if popped_element[0].right != None:
                queue.append((popped_element[0].right,popped_element[1]+1))

        return output
