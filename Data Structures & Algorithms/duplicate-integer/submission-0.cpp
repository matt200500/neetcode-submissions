class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int,int> numbers;
        for (int i = 0; i < nums.size(); ++i){
            auto it = numbers.find(nums[i]);
            if (it != numbers.end()){
                return true;
            }else{
                numbers[nums[i]] = i;
            }
        }
        return false;
    }
};
