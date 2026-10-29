class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total_product = 1
        total_zeros = 0
        for index, num in enumerate(nums):
            if num == 0:
                total_zeros += 1
            else:
                total_product = total_product * num
    
        for index, num in enumerate(nums):
            if num == 0:
                if total_zeros > 1: # if there are other 0s
                    output.append(0)
                else:
                    output.append(total_product) # append current product
            elif total_zeros > 0: # if there is a 0 in the product
                output.append(0)
            else:
                output.append(total_product // num)
        return output



