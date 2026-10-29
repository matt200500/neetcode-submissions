class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_string = ""
        for index, character in enumerate(s):
            if 25 >= (ord(character) - ord("A")) >= 0:
                alphanumeric_string += character.lower()
            elif 25 >= (ord(character) - ord("a")) >= 0:
                alphanumeric_string += character
            elif 9 >= (ord(character) - ord("0")) >= 0:
                alphanumeric_string += character
        if alphanumeric_string == alphanumeric_string[::-1]:
            return True
        return False
        