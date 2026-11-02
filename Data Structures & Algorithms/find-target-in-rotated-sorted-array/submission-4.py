class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_index = self.binary_search_rotation(nums,0,len(nums)-1)
        print("offset: ",start_index)

        return self.binary_search(nums,start_index,target,0,len(nums)-1)
    
    def binary_search_rotation(self,array,left,right) -> int:
        if left >= right:
            return left
        mid = left + (right - left) // 2
        if array[mid] > array[right]:
            return self.binary_search_rotation(array,mid+1,right)
        else:
            return self.binary_search_rotation(array,left,mid)
    
    def binary_search(self, array, offset, target, left, right) -> int:
        if left > right:
            return -1
        mid = left + (right - left) // 2
        true_mid_value = ((mid + offset) % len(array))
        
        if array[true_mid_value] == target:
            return true_mid_value
        elif array[true_mid_value] > target:
            return self.binary_search(array,offset,target,left,mid-1)
        else:
            return self.binary_search(array,offset,target,mid+1,right)
    
        
        
