#Approach - Use a sliding window that is k elements big, and iterate through nums. If nums is already in the window, return true, if not, then add it to the window. If the window becomes longer than k, then remove the indices that are too far apart
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True
            
            window.add(nums[i])

            if len(window)>k:
                window.remove(nums[i-k])

        return False
    