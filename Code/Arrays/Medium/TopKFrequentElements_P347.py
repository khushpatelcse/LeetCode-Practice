#Approach - Count the frequency of each number, and keep only the k most common

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostFrequent = Counter(nums).most_common(k)
        finalList = []
        for tuple in mostFrequent:
            finalList.append(tuple[0])
        return finalList