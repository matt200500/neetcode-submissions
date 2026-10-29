class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        std::vector<vector<int>> output;
        std::vector<int> current_subset;
        depth_first_search(0, nums, current_subset, output);
        return output;
    }

private: 
    void depth_first_search(int root, const vector<int>& nums, vector<int> current_subset, vector<vector<int>>& output){
        if (root >= nums.size()){
            output.push_back(current_subset);
            return;
        }

        depth_first_search(root+1, nums, current_subset, output);
        current_subset.push_back(nums[root]);
        depth_first_search(root+1, nums, current_subset, output);

    }

};

