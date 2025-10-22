#Approach - Use nested for loops to compare all combinations. If the combination equals the target, and does not equal each other, return it as the answer

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    return [i,j]