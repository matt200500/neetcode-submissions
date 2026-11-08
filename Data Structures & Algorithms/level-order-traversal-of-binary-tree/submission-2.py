# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        self.tree_mapping = {}
        self.dfs(root,0)
        for key,value in self.tree_mapping.items():
            output.append(value)
        return output

    def dfs(self,root,depth):
        if root == None:
            return
        if depth in self.tree_mapping:
            self.tree_mapping[depth].append(root.val)
        else:
            self.tree_mapping[depth] = [root.val]
        
        self.dfs(root.left,depth+1)
        self.dfs(root.right,depth+1)