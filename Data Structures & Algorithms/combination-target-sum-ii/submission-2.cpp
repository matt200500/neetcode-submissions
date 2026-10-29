class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> output;
        vector<int> current_combination;
        sort(candidates.begin(), candidates.end());
        depth_first_search(0, target, candidates, current_combination, output);
        return output;
    }

private:
    void depth_first_search( int root, int target, vector<int>& candidates, vector<int>& current_combination, vector<vector<int>>& output){
        if (target == 0){
            output.push_back(current_combination);
            return;
        }
        if (root >= candidates.size()){
            return;
        }
        for (int i = root; i < candidates.size();++i ){
            if (i > root && candidates[i] == candidates[i-1]){
                continue;
            }
            current_combination.push_back(candidates[i]);
            depth_first_search(i+1, target - candidates[i],candidates, current_combination, output);
            current_combination.pop_back();
        }
    }
};
