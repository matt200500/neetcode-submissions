class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            print(nums[i])
        for iterator in range(len(nums)):
            if iterator > 0 and nums[iterator] == nums[iterator - 1]: # if we have already seen this number
                continue
            elif nums[iterator] > 0: # if first number is greater than 0, break
                break
            
            left_pointer = iterator + 1
            right_pointer = len(nums) - 1

            while left_pointer < right_pointer:
                if nums[left_pointer] + nums[right_pointer] + nums[iterator] < 0:
                    left_pointer += 1
                elif nums[left_pointer] + nums[right_pointer]  + nums[iterator] > 0:
                    right_pointer -= 1
                else:
                    output.append([nums[iterator], nums[left_pointer], nums[right_pointer]])
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer+1]:
                        left_pointer += 1
                    while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer-1]:
                        right_pointer -= 1
                    left_pointer += 1
                    right_pointer -= 1


                
            
            
        return output
                


        