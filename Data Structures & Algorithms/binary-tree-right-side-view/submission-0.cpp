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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> output;
        if (root == nullptr){
            return output;
        }
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            std::vector<TreeNode*> next_row;
            while(!q.empty()){
                TreeNode* current = q.front();
                q.pop();
                if(current->left != nullptr){
                    next_row.push_back(current->left);
                }
                if(current->right != nullptr){
                    next_row.push_back(current->right);
                }
                if (q.empty()){
                    output.push_back(current->val);
                }
            }
            for(int i = 0; i < next_row.size();++i){
                q.push(next_row[i]);
            }
        }
        return output;
    }
};
