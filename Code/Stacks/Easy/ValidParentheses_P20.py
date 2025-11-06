#Approach - iterate through the string, if the current char is an opening bracket, add it to stack, if it is closing and matches with the previous bracket, then pop the previous. return not bracketStack to avoid edge case of "["
from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        bracketStack = []
        pairs = {"(":")", "[":"]", "{":"}"}

        for char in s:
            if char in pairs:
                bracketStack.append(char)
            elif char in pairs.values():
                if not bracketStack or pairs[bracketStack[-1]] != char:
                    return False
                bracketStack.pop()
            else:
                return False
        return not bracketStack