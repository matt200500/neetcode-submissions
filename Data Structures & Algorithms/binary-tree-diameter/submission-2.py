# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        output = self.get_diameter(root,0)
        return output[0]
        
    def get_diameter(self,root,max_diameter):
        if root == None:
            return max_diameter,0
        output = self.get_diameter(root.left,max_diameter)
        left_height = output[1]
        max_diameter = output[0]
        output = self.get_diameter(root.right,max_diameter)
        right_height = output[1]
        max_diameter = output[0]

        max_diameter = max(left_height + right_height, max_diameter)

        return max_diameter, (1 + max(left_height,right_height))