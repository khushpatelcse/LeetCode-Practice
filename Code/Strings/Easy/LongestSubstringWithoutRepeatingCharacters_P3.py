#Approach - Iterate through every char in the string, and append the remaining characters one by one, until the max length possible is found

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = list(s)
        maxLength = 0

        for i in range(len(chars)):
            substring = []
            currLength = 0
            while len(substring)==len(set(substring)) and i+currLength<len(chars):
                substring.append(chars[i+currLength])
                currLength+=1
            if maxLength<len(substring):
                maxLength = len(set(substring))
            if i+currLength==len(chars):
                return maxLength
        return maxLength