#Approach - Use two pointers to indicate the beginning and ending index for each new value, and iterate right until a new value is discovered, then iterate left once. This will leave us with no duplicates and ordered acsendingly on the left half of the array

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        right = 0
        left = 0

        while right < n:
            nums[left] = nums[right]

            while right < n and nums[left] == nums[right]:
                right += 1
            
            left += 1
        return left       
        