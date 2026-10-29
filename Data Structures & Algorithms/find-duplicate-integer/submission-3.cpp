class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        for (int i = 0 ; i < nums.size(); ++i){
            int number = abs(nums[i]);
            if (nums[number] < 0){
                return number;
            }
            nums[number] = nums[number] * -1;
        }
        return 0; 
    }
};
