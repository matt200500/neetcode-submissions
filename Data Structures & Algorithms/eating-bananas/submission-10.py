class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest_value = 0
        total_bannanas = 0 
        for index in range(len(piles)):
            largest_value = max(largest_value,piles[index])
            total_bannanas += piles[index]
        
        return self.binary_search(piles,h,math.ceil(total_bannanas / h),largest_value,largest_value)

    def binary_search(self, array, target, left, right,result):
        if left > right:
            return result
        mid = left + (right - left) // 2
        total_hours = self.eating_time(array,mid)

        if total_hours > target: # if total hours > h
            return self.binary_search(array,target,mid+1,right,result)
        elif total_hours <= target: # if total_hours <= h
            return self.binary_search(array,target,left,mid-1,mid)
    
    def eating_time(self,array,speed):
        total_hours = 0
        for index in range(len(array)):
            total_hours += math.ceil(array[index]/speed)
        return total_hours
