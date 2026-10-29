class Solution:

    def encode(self, strs: List[str]) -> str:
        output_string = ""
        for index,string in enumerate(strs):
            if string == "": 
                output_string += str((len(string))) + "#" + " "
            else:
                output_string += str((len(string))) + "#" + string
        return output_string
            
    def decode(self, s: str) -> List[str]:
        output = []
        if len(s) == 0:
            return output  

        current_string = ""
        character_length = ""
        character_length_as_int = -1
        new_string = True

        for index in range(len(s)):
            character = s[index]
            if new_string:
                if character == "#":
                    character_length_as_int = int(character_length)
                    character_length = "" # reset length
                    current_string = "" # reset string
                    new_string = False
                else:
                    character_length += character
            elif character_length_as_int == 0:
                output.append(current_string)
                new_string = True
            else:
                current_string += character
                character_length_as_int -= 1
                if character_length_as_int == 0:
                    output.append(current_string)
                    new_string = True
                    
        return output
