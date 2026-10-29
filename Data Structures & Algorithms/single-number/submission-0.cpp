class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int current_bit = nums[0];
        for (int i = 1; i < nums.size(); ++i){
            current_bit = current_bit ^ nums[i];
        }
        return current_bit;
    }
};
