class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> s_table;
        std::unordered_map<char, int> t_table;
        if (s.size() != t.size()){
            return false;
        }
        for (int i = 0; i < s.size(); ++i){
            auto s_it = s_table.find(s[i]);
            auto t_it = t_table.find(t[i]);
            if (s_it == s_table.end()){ // not in yet s
                s_table[s[i]] = 1;
            }else{
                ++s_table[s[i]];
            }
            if (t_it == t_table.end()){ // not in yet t
                t_table[t[i]] = 1;
            }else{
                ++t_table[t[i]];
            }
        }
        for (auto it = s_table.begin(); it != s_table.end(); ++it){
            auto t_it = t_table.find(it->first);
            if(t_it == t_table.end()){
                return false;
            }else if (t_it->second != it->second){
                return false;
            }
        }
        return true;
    }
};
