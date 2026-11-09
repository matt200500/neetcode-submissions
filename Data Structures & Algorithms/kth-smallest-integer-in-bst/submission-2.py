# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 1
        self.smallest = -1
        self.dfs(root,k)
        return self.smallest

    def dfs(self,root,k):
        if root == None:
            return 
        self.dfs(root.left,k)
        if self.counter == k:
            self.smallest = root.val
        self.counter += 1
        self.dfs(root.right,k)
