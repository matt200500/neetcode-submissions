class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.backtracking(nums,0,[])
        return self.output
    
    def backtracking(self,nums,index,current_list):
        if index == len(nums):
            self.output.append(current_list[:])
            return

        current_list.append(nums[index]) # add to current list
        self.backtracking(nums,index+1,current_list)
        current_list.pop()
        self.backtracking(nums,index+1,current_list) # dont add to current list
