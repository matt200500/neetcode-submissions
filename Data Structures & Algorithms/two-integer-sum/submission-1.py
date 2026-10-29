class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        i = 0
        while i < len(nums):
            difference = target - nums[i]
            if difference in seen_nums:
                return [seen_nums[difference],i]
            seen_nums[nums[i]] = i
            i+=1

        