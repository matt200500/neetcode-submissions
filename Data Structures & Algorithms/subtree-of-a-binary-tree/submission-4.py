# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.is_subtree = False
        self.dfs(root,subRoot)
        return self.is_subtree

    def dfs(self,root,subroot):
        if self.is_subtree == True:
            return
        if root == None:
            return
        if self.check_subtree(root,subroot):
            self.is_subtree = True
        self.dfs(root.left,subroot)
        self.dfs(root.right,subroot)
        
    def check_subtree(self,big_tree,small_tree) -> bool:
        if small_tree == None and big_tree == None: 
            return True
        elif small_tree == None:
            return False
        elif big_tree == None:
            return False
        elif big_tree.val != small_tree.val:
            return False
        if self.check_subtree(big_tree.left,small_tree.left) == False:
            return False
        if self.check_subtree(big_tree.right,small_tree.right) == False:
            return False
        return True
        


        