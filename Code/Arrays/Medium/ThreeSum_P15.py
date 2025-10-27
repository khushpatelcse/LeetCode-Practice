#Approach 1 - Use a for to iterate through the list, and treat i as a constant while applying the two pointer method
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        finalList = set()
        for i in range(len(nums)):
            leftPointer = i+1
            rightPointer = len(nums)-1
            target = -(nums[i])

            while(leftPointer<rightPointer):
                if nums[leftPointer]+nums[rightPointer]>target:
                    rightPointer-=1
                elif nums[leftPointer]+nums[rightPointer]<target:
                    leftPointer+=1
                elif nums[leftPointer]+nums[rightPointer]==target and i!=leftPointer and leftPointer!=rightPointer and rightPointer!=i:
                    finalList.add((nums[i],nums[leftPointer],nums[rightPointer]))
                    rightPointer-=1
                    leftPointer+=1
                else:
                    rightPointer-=1
                    leftPointer+=1

        return [list(i) for i in finalList]
    

#Approach 2 - (optimized)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        finalList = []
        
        for i in range(len(nums)-2): 
            if i>0 and nums[i]==nums[i-1]:
                continue

            leftPointer = i+1
            rightPointer = len(nums)-1

            while leftPointer<rightPointer:
                numSum = nums[i]+nums[leftPointer]+nums[rightPointer]

                if numSum<0:
                    leftPointer+=1
                elif numSum>0:
                    rightPointer-=1
                else :
                    finalList.append([nums[i], nums[leftPointer], nums[rightPointer]])
                    leftPointer+=1
                    rightPointer-=1
                    
                    while leftPointer<rightPointer and nums[leftPointer]==nums[leftPointer-1]:
                        leftPointer+=1
                    while leftPointer<rightPointer and nums[rightPointer]==nums[rightPointer+1]:
                        rightPointer-=1

        return finalList