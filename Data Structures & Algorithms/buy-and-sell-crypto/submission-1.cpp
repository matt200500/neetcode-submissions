class Solution {
public:
    int maxProfit(vector<int>& prices) {

        if (prices.size() == 0){
            return 0;
        }

        int current_min = prices[0];
        int min_index = 0;
        int output = 0;

        for(int i = 0; i < prices.size(); ++i){
            if (prices[i] - current_min > output){
                output = prices[i] - current_min;
            }
            if (prices[i] < current_min){
                current_min = prices[i];
            }
        }
        return output;
    }
};
