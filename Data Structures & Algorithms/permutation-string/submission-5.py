class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        left_index = 0
        s1_character_frequency = {}
        s2_character_frequency = {}
        matches = True

        for index in range(len(s1)):
            s1_character_frequency.setdefault(s1[index],0)
            s1_character_frequency[s1[index]] += 1

        for index in range(len(s2)):
            s2_character_frequency.setdefault(s2[index],0)
            s2_character_frequency[s2[index]] += 1

            if (index - left_index + 1) > len(s1):
                s2_character_frequency[s2[left_index]] -= 1
                if s2_character_frequency[s2[left_index]] == 0:
                    s2_character_frequency.pop(s2[left_index])
                left_index += 1
            
            for key,total in s1_character_frequency.items():
                if key in s2_character_frequency:
                    if total != s2_character_frequency[key]:
                        matches = False
                        break
                else:
                    matches = False
                    break
            if matches:
                return True
            matches = True

        return False
        