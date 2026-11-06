class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for index in range(len(nums)):
            number = abs(nums[index])
            if nums[number] < 0:
                return number
            nums[number] = nums[number] * -1

        return 0