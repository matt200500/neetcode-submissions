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
    int kthSmallest(TreeNode* root, int k) {
        vector<int> array;
        DFS(root, array);
        return array[k-1];
    }
private:
    void DFS(TreeNode* root, vector<int>& array){
        if(root == nullptr){
            return;
        }
        DFS(root->left, array);
        array.push_back(root->val);
        DFS(root->right, array);
    }
};
