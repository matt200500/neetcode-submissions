class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.digit_mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if len(digits) == 0:
            return []
        self.output = []
        self.backtrack(digits,0,[])
        return self.output

    def backtrack(self,digits,index,current_string):
        if index == len(digits):
            self.output.append("".join(current_string))
            return

        # add first character
        current_string.append(self.digit_mappings[digits[index]][0])
        self.backtrack(digits,index+1,current_string)
        current_string.pop()

        # add second character
        current_string.append(self.digit_mappings[digits[index]][1])
        self.backtrack(digits,index+1,current_string)
        current_string.pop()
    
        # add third character
        current_string.append(self.digit_mappings[digits[index]][2])
        self.backtrack(digits,index+1,current_string)
        current_string.pop()
    
        if digits[index] == "7" or digits[index] == "9":
            # add fourth character
            current_string.append(self.digit_mappings[digits[index]][3])
            self.backtrack(digits,index+1,current_string)
            current_string.pop()

        