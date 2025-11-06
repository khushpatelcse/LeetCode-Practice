#Approach - Cast the int to a string, and compare the original string to the reversed string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)=="".join(reversed(str(x)))