class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = set()
        longest_substring = 0
        left_index = 0

        for index in range(len(s)):
            if s[index] in current_substring:
                longest_substring = max(longest_substring,len(current_substring))
                while s[left_index] != s[index]:
                    current_substring.remove(s[left_index])
                    left_index += 1
                current_substring.remove(s[left_index])
                left_index += 1
                current_substring.add(s[index])
            else:
                current_substring.add(s[index])
        
        longest_substring = max(longest_substring,len(current_substring))
        return longest_substring

# abcdefcoplkijuhy