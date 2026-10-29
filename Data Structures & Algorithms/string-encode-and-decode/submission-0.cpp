class Solution {
public:

    string encode(vector<string>& strs) {
        std::string output;
        for (int i = 0; i < strs.size(); ++i){
            output.append(strs[i]);
            output.append("漢");

        }
        return output;
    }

    vector<string> decode(string s) {
        std::vector<string> output;
        std::string delimiter = "漢";
        auto pos = s.find(delimiter);
        
        while (pos != string::npos){
            output.push_back(s.substr(0,pos));
            s.erase(0, pos + delimiter.length());
            pos = s.find(delimiter);
        }

        return output;
    }
};
