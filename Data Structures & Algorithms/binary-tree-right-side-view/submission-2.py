# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_only = []
        if root == None:
            return right_side_only
        queue = deque()
        queue.append(root)
        while len(queue) != 0:
            level = []
            for i in range(len(queue)):
                popped_node = queue.popleft()
                level.append(popped_node.val)
                if popped_node.left != None:
                    queue.append(popped_node.left)
                if popped_node.right != None:
                    queue.append(popped_node.right)
            right_side_only.append(level[-1])
        return right_side_only
            

        
        