class Solution {
public:
    bool isPalindrome(string s) {
        auto left_pointer = s.begin();
        auto right_pointer = --s.end();
        while(!((*left_pointer >= 65 && *left_pointer <= 90) || (*left_pointer >= 97 && *left_pointer <= 122) || (*left_pointer >= 48 && *left_pointer <= 57))){
            ++left_pointer;
        }
        while(!((*right_pointer >= 65 && *right_pointer <= 90) || (*right_pointer >= 97 && *right_pointer <= 122) || (*right_pointer >= 48 && *right_pointer <= 57))){
            --right_pointer;
        }

        while(left_pointer <= right_pointer){
            cout << "we enter\n";
            while(!((*left_pointer >= 65 && *left_pointer <= 90) || (*left_pointer >= 97 && *left_pointer <= 122) || (*left_pointer >= 48 && *left_pointer <= 57))){
                ++left_pointer;
            }
            while(!((*right_pointer >= 65 && *right_pointer <= 90) || (*right_pointer >= 97 && *right_pointer <= 122) || (*right_pointer >= 48 && *right_pointer <= 57))){
                --right_pointer;
            }
            cout << "left is: " << *left_pointer << " right is: " << *right_pointer << "\n";
            if (std::tolower(*right_pointer) != std::tolower(*left_pointer)){
                return false;
            }
            ++left_pointer;
            --right_pointer;
        }
        return true;
    }
};
