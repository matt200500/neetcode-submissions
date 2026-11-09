# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.current_index = 0
        self.inorder_map = {}
        for index,value in enumerate(inorder):
            self.inorder_map[value] = index
        
        return self.copy_tree(preorder,inorder,0,len(inorder)-1)

    def copy_tree(self,preoder,inorder,left_index,right_index):
        if left_index > right_index:
            return None
        current_root = TreeNode()
        current_root.val = preorder[self.current_index]
        self.current_index += 1

        inorder_index = self.inorder_map[current_root.val]
        
        current_root.left = self.copy_tree(preorder,inorder,left_index,inorder_index-1)
        current_root.right = self.copy_tree(preoder,inorder,inorder_index+1,right_index)

        return current_root
       
        
        
        
        


        