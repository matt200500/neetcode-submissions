class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        character_frequency = {}
        largest_character = 0
        left_index = 0
        longest_substring = 0

        for index in range(len(s)):
            value = character_frequency.setdefault(s[index],0)
            character_frequency[s[index]] += 1

            largest_character = max(largest_character, character_frequency[s[index]])
            if ((index - left_index + 1) - largest_character) > k: # if we have too many characters
                character_frequency[s[left_index]] -= 1
                left_index += 1
            longest_substring = max(longest_substring,index - left_index + 1)
        
        return longest_substring
            





        return max(longest_substring,longest_substring)
                



        