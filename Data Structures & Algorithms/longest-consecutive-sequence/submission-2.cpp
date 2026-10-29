class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> numbers(nums.begin(),nums.end());
        int output = 0;
        
        for (int i = 0; i < numbers.size(); ++i){
            auto it = numbers.begin();
            advance(it, i);
            if (numbers.find(*it -1) == numbers.end()){
                int new_output = 1;
                int current_number = *it;
                while(numbers.find(current_number+ 1) != numbers.end()){  
                    ++new_output;
                    ++current_number;
                }
                output = max(output,new_output);
            }
        }
        return output;
    }
};
