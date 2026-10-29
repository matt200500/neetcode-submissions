class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = {}
        t_counts = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_char = s[i]
            s_counts[s_char] = s_counts.get(s_char, 0) + 1
            
            t_char = t[i]
            t_counts[t_char] = t_counts.get(t_char, 0) + 1

        for char, value in s_counts.items():
            if char in t_counts:
                if t_counts[char] != value:
                    return False
            else:
                return False
        return True
        





        