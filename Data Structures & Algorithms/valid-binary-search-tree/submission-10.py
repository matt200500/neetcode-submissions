# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid_tree = True
        if root == None:
            return True
        self.dfs(root,-1000000001,1000000001)
        return self.is_valid_tree

    def dfs(self,root,left_bound,right_bound):

        if root.left != None:
            self.dfs(root.left,left_bound,root.val)
        if root.right != None:
            self.dfs(root.right,root.val,right_bound)

        if left_bound >= root.val or root.val >= right_bound:
            self.is_valid_tree = False
        


        
        