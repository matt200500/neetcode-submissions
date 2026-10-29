/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (root == nullptr){
            return false;
        }
        if(DFS(root, subRoot)){
            return true;
        }
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }

private:
    bool DFS(TreeNode* p, TreeNode* q){
        if(p == nullptr && q == nullptr){
            return true;
        }
        if(q == nullptr && p != nullptr){
            return false;
        }
        if(q != nullptr && p == nullptr){
            return false;
        }
        
        if(p->val != q->val){
            return false;
        }

        if (DFS(p->left, q->left) == true && DFS(p->right, q->right) == true){
            return true;
        }
        return false;
    }
};
