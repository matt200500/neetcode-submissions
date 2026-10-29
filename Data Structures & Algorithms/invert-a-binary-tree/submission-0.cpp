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
    TreeNode* invertTree(TreeNode* root) {
        return depth_first_search(root);
    }

private:
    TreeNode* depth_first_search(TreeNode* root){
        std::unordered_set<TreeNode*> visited;
        std::deque<TreeNode*> stack;
        if(root == nullptr){
            return root;
        }

        stack.push_back(root);

        while(!stack.empty()){
            TreeNode* top = stack.back();
            stack.pop_back();

            std::swap(top->left, top->right);
            if (top->left != nullptr){
                stack.push_back(top->left);
            }
            if(top->right != nullptr){
                stack.push_back(top->right);
            }  
        }
        return root;
    }
};
