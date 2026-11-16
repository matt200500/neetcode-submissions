class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        taken_numbers = [False] * len(nums)
        self.backtrack(nums,[],taken_numbers)

        return self.output


    def backtrack(self,nums,current_list,taken_numbers):
        if len(current_list) == len(nums):
            self.output.append(current_list[:])
            return
        
        for index in range(len(nums)):
            if taken_numbers[index] == True:
                continue
            
            current_list.append(nums[index])
            taken_numbers[index] = True
            self.backtrack(nums,current_list,taken_numbers)

            taken_numbers[index] = False
            current_list.pop()
        
