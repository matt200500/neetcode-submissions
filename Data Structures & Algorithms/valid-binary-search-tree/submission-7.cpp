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
    bool isValidBST(TreeNode* root) {
        return DFS(root, LONG_MAX, LONG_MIN);
    }
private:
    bool DFS(TreeNode* root, long max, long min){
        if (root == nullptr){
            return true;
        }
        if(root->val >= max || root->val <= min){
            return false;
        }
        return DFS(root->left, root->val,min) && DFS(root->right, max, root->val);
    }
};
