class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> output;
        int left_pointer = 0;
        int right_pointer = numbers.size() -1;
        while(left_pointer < right_pointer){
            if (numbers[left_pointer] + numbers[right_pointer] > target){
                --right_pointer;
            }else if (numbers[left_pointer] + numbers[right_pointer] < target){
                ++left_pointer;
            }else{
                output.push_back(left_pointer + 1);
                output.push_back(right_pointer + 1);
                return output;
            }
        }
        return output;
    }
};
