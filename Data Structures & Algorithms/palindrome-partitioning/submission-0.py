class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.output = []
        self.backtrack(s,0,0,[[]])
        return self.output

    def backtrack(self,original_string,start_index,current_index,string_list):
        if current_index == len(original_string):
            if self.check_palindrome(string_list[-1]): # if final added string is a palindrome
                new_list = []
                for index in range(len(string_list)):
                    new_list.append("".join(string_list[index]))
                self.output.append(new_list)
            return
        
        # add to current_string
        string_list[-1].append(original_string[current_index])
        self.backtrack(original_string,start_index,current_index+1,string_list)
        string_list[-1].pop()

        # create a new string
        if self.check_palindrome(string_list[-1]): # if the last string added is a palindrome
            string_list.append([original_string[current_index]])
            self.backtrack(original_string,current_index,current_index+1,string_list)
            string_list.pop()
 


    def check_palindrome(self, string) -> bool:
        if len(string) == 0:
            return False
        left = 0
        right = len(string) -1
        while left <= right:
            if string[left] != string[right]:
                return False
            left += 1
            right -=1 
        return True
