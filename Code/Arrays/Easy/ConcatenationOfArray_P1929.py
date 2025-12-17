from typing import List

#Approach 1 - Reappend the array to the new array

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans
    
#Approach 2 (Optimal) - Add the array twice

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums