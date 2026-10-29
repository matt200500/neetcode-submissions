class Solution {
public:
    int hammingWeight(uint32_t n) {
        int output = 0;
        uint32_t mask = 1u << 0;
        for (int i = 0; i < 32; ++i){
            if (n & mask){
                ++output;
            }
            mask = mask << 1;
        }
        return output;
    }
};
