# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lca = root
        self.p_depth = 101
        self.q_depth = 101
        self.dfs(root,p,q,1)
        return self.lca

    def dfs(self,root,p,q,depth):
        if root == None:
            return
        if p.val == root.val:
            self.p_depth = depth
        if q.val == root.val:
            self.q_depth = depth

        if depth > self.q_depth or depth > self.p_depth: # if depth too great
            return
        if p.val >= root.val and q.val >= root.val: # both greater
            self.lca = root
            self.dfs(root.right,p,q,depth+1)
        elif p.val <= root.val and q.val <= root.val: # both less
            self.lca = root
            self.dfs(root.left,p,q,depth+1)
        else: # 1 greater and 1 less
            self.lca = root
        
    


        