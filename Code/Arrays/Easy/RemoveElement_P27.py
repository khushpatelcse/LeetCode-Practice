#Approach - Use two pointers to replace all the instances of val with the value from the right pointer. Decrement right when value is used, or it is equal to val, increment left when used

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        right = n-1
        left = 0

        while left <= right:

            if nums[left]==val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1

        return right+1