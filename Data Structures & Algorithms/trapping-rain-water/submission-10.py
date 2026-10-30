class Solution:
    def trap(self, height: List[int]) -> int:
        left_largest = []
        right_largest = [0] * len(height)
        max_left_height = -1
        max_right_height = -1
        output = 0
        for index in range(len(height)): # get the max left heigt for each cell
            left_largest.append(max_left_height)
            max_left_height = max(max_left_height,height[index])
        
        for index in range(len(height)-1,-1,-1): # get max right height for each cell
            right_largest[index] = max_right_height
            max_right_height = max(max_right_height,height[index])

        for index in range(len(height)): # update output

            if index == 0 or index == (len(height) - 1): # if we are an edge
                continue
        
            output += max(0,(min(left_largest[index],right_largest[index]) - height[index]))
            
        return output


        