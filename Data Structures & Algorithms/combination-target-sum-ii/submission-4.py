class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = []
        candidates.sort()
        self.backtracking(candidates,0,target,[])
        return self.output

    def backtracking(self,nums,index,target,current_list):
        if target == 0:
            self.output.append(current_list[:])
            return
        if index >= len(nums) or target < 0:
            return
        

        # choose to add current index
        current_list.append(nums[index])
        self.backtracking(nums,index+1,target - nums[index],current_list)

        # choose to not add current index
        current_list.pop()
        while index < len(nums) -1 and nums[index] == nums[index+1]:
            index += 1
        self.backtracking(nums,index+1,target,current_list)
        