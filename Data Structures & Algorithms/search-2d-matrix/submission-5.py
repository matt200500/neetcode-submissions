class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_length = len(matrix[0])
        total_matrix = len(matrix)
        return self.binary_search_matrix(matrix,target,0,len(matrix)-1)


        
    def binary_search_matrix(self,matrix,target,left,right) -> bool:
        if left > right:
            return False
        mid = left + (right - left) // 2
        if target >= matrix[mid][0] and target <= matrix[mid][-1]: # binary search in array if target inside array
            return self.binary_search(matrix[mid],target,0,len(matrix[mid])-1)
        elif target > matrix[mid][-1]: # if target larger than largest value in mid array
            return self.binary_search_matrix(matrix,target,mid+1,right)
        else: # if target smaller than smallest value in mid array
            return self.binary_search_matrix(matrix,target,left,mid-1)
    
    def binary_search(self,array,target,left,right) -> bool:
        if left > right:
            return False
        mid = left + (right - left) // 2
        if target == array[mid]:
            return True
        elif target > array[mid]:
            return self.binary_search(array,target,mid+1,right)
        else:
            return self.binary_search(array,target,left,right-1)

        

        