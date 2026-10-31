class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for index in range(len(s)):
            string = s[index]
            stack_top = "0"
            if len(stack) != 0:
                stack_top = stack[-1]
            if string == "(" or string == "[" or string == "{":
                stack.append(string)
            elif string == ")":
                if stack_top == "(":
                    stack.pop(-1)
                else:
                    return False
            elif string == "]":
                if stack_top == "[":
                    stack.pop(-1)
                else:
                    return False
            elif string == "}":
                if stack_top =="{":
                    stack.pop(-1)
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False


        