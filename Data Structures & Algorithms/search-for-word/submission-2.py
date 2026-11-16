class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.is_valid = False
        
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == word[0]:
                    taken_values = [[False] * len(board[0]) for x in range(len(board))]
                    taken_values[row][column] = True
                    self.backtracking(board,word,1,row,column,taken_values)
                    if self.is_valid: # return early if first found char is true
                        return self.is_valid

        return self.is_valid
        
    def backtracking(self,board,word,index,row,column,taken_values):
        if self.is_valid:
            return

        if index == len(word):
            self.is_valid = True
            return
        
        if row < len(board) -1 and board[row+1][column] == word[index] and taken_values[row+1][column] == False: # down
            taken_values[row+1][column] = True
            self.backtracking(board,word,index+1,row+1,column,taken_values)
            taken_values[row+1][column] = False
        if column < len(board[0]) -1 and board[row][column+1] == word[index] and taken_values[row][column+1] == False: # right
            taken_values[row][column+1] = True
            self.backtracking(board,word,index+1,row,column+1,taken_values)
            taken_values[row][column+1] = False
        if row > 0 and board[row-1][column] == word[index] and taken_values[row-1][column] == False: # up
            taken_values[row-1][column] = True
            self.backtracking(board,word,index+1,row-1,column,taken_values)
            taken_values[row-1][column] = False
        if column > 0 and board[row][column-1] == word[index] and taken_values[row][column-1] == False: # left
            taken_values[row][column-1] = True
            self.backtracking(board,word,index+1,row,column-1,taken_values)
            taken_values[row][column-1] = False



        