#Approach - Remove any non-alphanumeric characters, make it lowercase, and compare it to the reversed version
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"\W+", "", s).replace("_", "").lower()
        return s==("".join(reversed(s)))
    