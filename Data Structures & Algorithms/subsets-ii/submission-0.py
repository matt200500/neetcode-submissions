class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        nums.sort()
        self.backtrack(nums,0,[])
        return self.output

    def backtrack(self,nums,index,current_list):
        if index >= len(nums):
            self.output.append(current_list[:])
            return
        
        current_list.append(nums[index])
        self.backtrack(nums,index+1,current_list)

        current_list.pop()
        while index < len(nums)-1 and (nums[index] == nums[index+1]):
            index += 1
        self.backtrack(nums,index+1,current_list)
        