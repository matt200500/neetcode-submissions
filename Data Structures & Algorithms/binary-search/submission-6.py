class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums,target,0,len(nums) -1)
    
    def binary_search(self, array, target, left, right) -> int:
        if left > right:
            return -1
        mid = left + (right - left) // 2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            return self.binary_search(array,target,mid+1,right)
        else:
            return self.binary_search(array,target,left,mid -1)