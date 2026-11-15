class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.output = []
        self.backtracking(nums,0,target,[],0)
        return self.output

    def backtracking(self,nums,index,target,current_list,current_sum):
        if current_sum > target or index >= len(nums):
            return
        if current_sum == target:
            self.output.append(current_list[:])
            return
        
        # add number to sum and keep index on same number
        current_list.append(nums[index])
        self.backtracking(nums,index,target,current_list,current_sum + nums[index]) 
        
        # move on to next number and dont add current number to sum
        current_list.pop()
        self.backtracking(nums,index +1,target,current_list,current_sum)
        