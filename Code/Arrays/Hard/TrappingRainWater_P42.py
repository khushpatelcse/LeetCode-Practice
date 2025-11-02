#Approach - Find the highest wall for the left and right of each index, and sum the amount of water based on the lower wall and height of current index

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        total = 0
        n = len(height)

        #Get the left max, and right max for current index
        leftMax, rightMax = [0]*n, [0]*n
        currMax = 0
        for i in range(n):
            currMax = max(currMax, height[i])
            leftMax[i] = currMax
        currMax = 0
        for i in range(n-1, -1, -1):
            currMax = max(currMax, height[i])
            rightMax[i] = currMax

        #Add the highest amount of water possible, based on current iterations lowest wall
        for i in range(n):
            trapped = min(leftMax[i], rightMax[i]) - height[i]
            if trapped:
                total+=trapped
    
        return total
    

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))