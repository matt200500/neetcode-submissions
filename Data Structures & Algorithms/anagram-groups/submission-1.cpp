class Solution {

struct VectorHash {
size_t operator()(const vector<int>& v) const {
    size_t hash = 0;
    for (int num : v) {
        hash ^= hash * 31 + num; // Simple hash combination
    }
    return hash;
}
};

public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<vector<int>,vector<string>, VectorHash> all_strings;

        for (int i = 0; i < strs.size(); ++i){
            std::vector<int> char_count;
            std::string current_string = strs[i];

            for (int y = 0; y < current_string.size(); ++y){
                int char_ascii = current_string[y];
                char_count.push_back(char_ascii);
            }

            std::sort(char_count.begin(), char_count.end());
            auto it = all_strings.find(char_count);
            std::vector<string> stuff;
            all_strings[char_count].push_back(current_string);
        }
        std::vector<std::vector<string>> output;
        for (auto it = all_strings.begin(); it != all_strings.end(); ++it){
            output.push_back(it->second);
        }
        return output;
    }  
};
