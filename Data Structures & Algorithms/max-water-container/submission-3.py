class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(heights) - 1
        max_water = 0
        previous_water = 0
        while left_pointer < right_pointer:
            current_height = self.getWater(heights,left_pointer,right_pointer)
            max_water = max(max_water,current_height)

            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_water

    def getWater(self,heights: List[int],left_pointer: int,right_pointer: int) -> int:
        return min(heights[left_pointer],heights[right_pointer]) * (right_pointer - left_pointer)
