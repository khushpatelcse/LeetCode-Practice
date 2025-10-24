#Approach 1 - If the sorted strings are equal, they are anagram, else they are not
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
    
#Approach 2 - Compare Counter() - *optimized*
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)