class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        left_extrude_index = [-1] * len(heights)
        right_extrude_index = [len(heights)] * len(heights)
        largest_rectangle = 0

        for index in range(len(heights)): # right heights
            if len(stack) == 0:
                stack.append(index)
                continue
            
            while len(stack) != 0 and heights[index] < heights[stack[-1]]:
                popped_index = stack.pop()
                right_extrude_index[popped_index] = index
            
            stack.append(index)
        
        stack = []
        for index in range(len(heights)-1,-1,-1): # right heights
            if len(stack) == 0:
                stack.append(index)
                continue
            while len(stack) != 0 and heights[index] < heights[stack[-1]]:
                popped_index = stack.pop()
                left_extrude_index[popped_index] = index
            
            stack.append(index)

        for index in range(len(heights)):
            rectangle_size = (right_extrude_index[index] - left_extrude_index[index] - 1) * heights[index]
            largest_rectangle = max(largest_rectangle,rectangle_size)

        return largest_rectangle
