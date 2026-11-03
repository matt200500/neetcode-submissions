class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = {}
        longest_substring = 0

        for index in range(len(s)):
            if s[index] in current_substring:
                longest_substring = max(longest_substring,len(current_substring))
                while current_substring and next(iter(current_substring)) != s[index]:
                    key = next(iter(current_substring))
                    current_substring.pop(key)
                key = next(iter(current_substring))
                current_substring.pop(key)
                current_substring[s[index]] = index
            else:
                current_substring[s[index]] = index
        
        longest_substring = max(longest_substring,len(current_substring))
        return longest_substring

# abcdefcoplkijuhy