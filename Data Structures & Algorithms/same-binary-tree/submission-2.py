# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.is_equal = True
        self.dfs(p,q)
        return self.is_equal

    def dfs(self,left_node,right_node):

        if left_node == None and right_node == None:
            return
        elif left_node == None:
            self.is_equal = False
            return
        elif right_node == None:
            self.is_equal = False
            return
        elif left_node.val != right_node.val:
            self.is_equal = False
            return
        
        self.dfs(left_node.left,right_node.left)
        self.dfs(left_node.right,right_node.right)
        
        