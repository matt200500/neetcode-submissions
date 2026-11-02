class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.binary_search(nums,0,len(nums)-1)

    def binary_search(self,array,left, right) -> int:
        if left >= right:
            return array[left]
        mid = left + (right - left) // 2
        print(array[mid])
        if array[mid] > array[right]:
            return self.binary_search(array,mid+1,right)
        else:
            return self.binary_search(array,left,mid)

        
        