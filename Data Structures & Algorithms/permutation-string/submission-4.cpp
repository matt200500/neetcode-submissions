class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if(s1.size() > s2.size()){
            return false;
        }
        std::vector<int> frequency_s1(26,0);
        std::vector<int> frequency_substring(26,0);
        for (int i = 0; i < s1.size(); ++i){
            ++frequency_s1[s1[i] - 'a'];
        }

        int left_pointer = 0;
        for (int i = 0; i < s2.size(); ++i){

            ++frequency_substring[s2[i] - 'a'];

            while((i - left_pointer + 1) > s1.size()){ // while window too large
                --frequency_substring[s2[left_pointer] - 'a'];
                ++left_pointer;
            }

            if(frequency_substring == frequency_s1){
                return true;
            }
        }
        return false;
    }
};
