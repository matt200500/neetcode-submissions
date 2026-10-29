class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left_pointer = 0;
        int right_pointer = heights.size() -1;
        int max_area = 0;
        while (left_pointer < right_pointer){
            int current_area = (right_pointer - left_pointer) * min(heights[left_pointer], heights[right_pointer]);
            if(max_area < current_area){
                max_area = current_area;
            }
            if (heights[left_pointer] < heights[right_pointer]){
                ++left_pointer;
            }else{
                --right_pointer;
            }
        }
        return max_area;
    }
};
