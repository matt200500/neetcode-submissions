class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen_nums = {}
        for index, number in enumerate(numbers, start = 1):
            difference = target - number
            if difference in seen_nums:
                return [seen_nums[difference],index]
            seen_nums[number] = index
        