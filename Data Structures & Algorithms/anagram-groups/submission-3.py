class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        similar_strings = {}
        for string in strs:
            alphabet = [0] * 26
            for i in range(len(string)):
                alphabet[ord(string[i]) - ord('a')] += 1
            
            hashed_alphabet = tuple(alphabet)
            current_list = similar_strings.get(hashed_alphabet, [])
            current_list.append(string)
            similar_strings[hashed_alphabet] = current_list
        for key,value in similar_strings.items():
            output.append(value)
        return output
            

        