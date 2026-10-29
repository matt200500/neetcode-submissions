class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_dictionary = {}
        square_dictionary = {}
        
        square_set = set()
        for row, array in enumerate(board):
            row_set = set() # make an empty set for the row
            for column, number in enumerate(array):
            
                # row check
                if number in row_set and number != ".": # if row already contains a duplicate
                    return False
                row_set.add(number)

                # column check
                if column in column_dictionary and number in column_dictionary[column] and number != ".":
                    return False
                
                # add number to set and if set doesnt exist, initialize a new one
                column_dictionary.setdefault(column, set()).add(number) 

                # square check
                square_dictionary_area = (row // 3, column // 3)
                if square_dictionary_area in square_dictionary and number in square_dictionary[square_dictionary_area] and number != ".":
                    return False
                
                square_dictionary.setdefault(square_dictionary_area,set()).add(number)

        return True
