# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0
        self.dfs(root,-101)
        return self.good_nodes

    def dfs(self,root,max_value):
        if root == None:
            return
        if root.val >= max_value:
            self.good_nodes += 1
        max_value = max(root.val,max_value)
        self.dfs(root.left,max_value)
        self.dfs(root.right,max_value)

        
        

        