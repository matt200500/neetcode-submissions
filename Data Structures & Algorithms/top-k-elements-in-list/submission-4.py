class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequent_elemets = {}
        most_frequent_counts = [[] for _ in range(len(nums) + 1)]        
        output = []
        for i in range(len(nums)):
            most_frequent_elemets[nums[i]] = most_frequent_elemets.get(nums[i], 0) + 1
        
        for number, count in most_frequent_elemets.items():
            most_frequent_counts[count].append(number)
        
        i = len(most_frequent_counts) - 1
        while i > -1:
            output.extend(most_frequent_counts[i])
            k -= len(most_frequent_counts[i])
            if k <= 0:
                return output
            i -= 1

        