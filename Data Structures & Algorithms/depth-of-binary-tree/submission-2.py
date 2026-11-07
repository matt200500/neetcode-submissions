# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.get_depth(root,1)
    
    def get_depth(self,root,current_depth) -> int:
        left_depth = 0
        right_depth = 0
        if root.left != None:
            left_depth = self.get_depth(root.left,current_depth+1)
        if root.right != None:
            right_depth = self.get_depth(root.right,current_depth+1)

        return max(current_depth,left_depth,right_depth)
        


        