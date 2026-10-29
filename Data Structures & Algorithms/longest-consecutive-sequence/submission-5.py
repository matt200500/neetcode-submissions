class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        starting_points = set()
        longest_sequence = 0

        for number in range(len(nums)): # add all numbers to a set
            nums_set.add(nums[number])
        for number in nums_set: # get all valid starting numbers
            if not (number - 1 in nums_set):
                starting_points.add(number)
        for number in starting_points:
            valid_sequence = True
            current_number = number
            current_sequence = 1
            while valid_sequence:
                if current_number + 1 in nums_set:
                    current_number += 1
                    current_sequence += 1
                else:
                    valid_sequence = False
            longest_sequence = max(longest_sequence, current_sequence)
        
        return longest_sequence



        