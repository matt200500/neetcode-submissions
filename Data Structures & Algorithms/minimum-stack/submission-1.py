class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest_value_index = -1
        
    def push(self, val: int) -> None:
        self.stack.append((val,self.smallest_value_index))
        # if stack is empty or variable is the new smallest
        if self.smallest_value_index == -1 or val < self.stack[self.smallest_value_index][0]:
            self.smallest_value_index = len(self.stack) - 1


    def pop(self) -> None:
        top = self.stack.pop(-1)
        if len(self.stack) == 0: # reset smallest value to default if empty
            self.smallest_value_index = -1
        elif self.smallest_value_index == len(self.stack): # if top was smallest index
            self.smallest_value_index = top[1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.smallest_value_index == -1:
            return self.stack[0][0]
        return self.stack[self.smallest_value_index][0]
        
