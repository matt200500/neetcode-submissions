# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recurse(root)
        return root
    
    def recurse(self, root):
        if root == None or root.left == None and root.right == None:
            return

        left = root.left
        root.left = root.right
        root.right = left

        self.recurse(root.left)
        self.recurse(root.right)