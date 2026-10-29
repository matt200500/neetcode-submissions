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
        for (int y = 0; y < frequency_s1.size(); ++y){
                cout << frequency_s1[y] << " ";
            }
            cout << "\ns1 size = " << s1.size()<< "\n";
        int left_pointer = 0;
        for (int i = 0; i < s2.size(); ++i){

            ++frequency_substring[s2[i] - 'a'];

            while((i - left_pointer + 1) > s1.size()){ // while window too large
                cout << "ppp\n";
                --frequency_substring[s2[left_pointer] - 'a'];
                ++left_pointer;
            }
            
            for (int y = 0; y < frequency_substring.size(); ++y){
                cout << frequency_substring[y] << " ";
            }
            cout << "\n i = " << i << " left = " << left_pointer << "\n";

            if(frequency_substring == frequency_s1){
                return true;
            }
        }
        return false;
    }
};
