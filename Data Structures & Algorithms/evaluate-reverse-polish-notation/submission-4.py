class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for index in range(len(tokens)):
            variable = tokens[index]
            if variable == "+":
                second_number = stack.pop()
                first_number = stack.pop()
                stack.append(first_number + second_number)
            elif variable == "-":
                second_number = stack.pop()
                first_number = stack.pop()
                stack.append(first_number - second_number)
            elif variable == "*":
                second_number = stack.pop()
                first_number = stack.pop()
                stack.append(first_number * second_number)
            elif variable == "/":
                second_number = stack.pop()
                first_number = stack.pop()
                stack.append(int(first_number / second_number))
            else:
                stack.append(int(variable))
        return stack[-1]