class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        
        for index in range(len(temperatures)):
            current_temp = temperatures[index]
            if len(stack) == 0: # if stack is empty
                stack.append(index)
            else:
                 # while current is greater than top and not zero
                while len(stack) != 0 and current_temp > temperatures[stack[-1]]:
                    top = stack.pop()
                    output[top] = index - top

                stack.append(index) # add to the stack

        return output

        