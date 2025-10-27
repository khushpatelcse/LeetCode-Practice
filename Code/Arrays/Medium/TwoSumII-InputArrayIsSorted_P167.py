#Approach - Create a pointer for the highest and lowest, and compare the sum to the target. If target is less than sum, decrement the right pointer, if it is greater then increment the left pointer. Iterate until the solution is found

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while(numbers[left]+numbers[right] != target):
            if (numbers[left]+numbers[right] > target):
                right-=1
            else:
                left+=1
        return [left+1, right+1]