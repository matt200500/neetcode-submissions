class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        combined = list(zip(position, speed))
        combined.sort(key=self.get_key)
        position, speed = zip(*combined)

        stack = []
        for index in range(len(position)-1,-1,-1): # sort from farthest position
            if len(stack) == 0:
                stack.append(index)
            else:
                time_taken = self.get_time_taken(target, speed[index], position[index])
                if time_taken > self.get_time_taken(target, speed[stack[-1]],position[stack[-1]]):
                    stack.append(index)
        return len(stack)


    def get_key(self,x):
        return x[0]
    
    def get_time_taken(self,target,speed,position) -> int:
        return (target - position) / speed





