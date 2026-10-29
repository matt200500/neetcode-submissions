class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,int> numbers;
        for (int i = 0; i < nums.size();++i){
            int difference = target - nums[i];
            auto difference_it = numbers.find(difference);
            if (difference_it != numbers.end()){
                std::vector<int> output;
                output.push_back(difference_it->second);
                output.push_back(i);
                return output;
            }
            auto it = numbers.find(nums[i]);
            if (it == numbers.end()){
                numbers[nums[i]] = i;
            }
        }

    }
};
