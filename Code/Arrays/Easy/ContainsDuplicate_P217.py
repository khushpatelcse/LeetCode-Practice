#Approach - If the length of the list is the same as the set of the list, then there are no duplicates, otherwise there is at least one duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))