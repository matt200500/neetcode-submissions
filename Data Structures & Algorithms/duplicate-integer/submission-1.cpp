class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> numbers;
        for (int i = 0; i < nums.size(); ++i){
            numbers.insert(nums[i]);
        }
        if (nums.size() != numbers.size()){
            return true;
        }
        return false;
    }
};