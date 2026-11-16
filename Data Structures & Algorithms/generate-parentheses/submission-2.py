class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.output = []
        self.backracking(n,n,[])
        return self.output

    def backracking(self,total_open,total_close,current_string):
        if total_open == 0 and total_close == 0:
            self.output.append("".join(current_string))
            return

        if total_open > 0:
            current_string.append("(")
            self.backracking(total_open - 1,total_close,current_string) 
            current_string.pop()

        if total_close > 0 and total_close > total_open:
            current_string.append(")")
            self.backracking(total_open,total_close - 1,current_string)
            current_string.pop()



    
        