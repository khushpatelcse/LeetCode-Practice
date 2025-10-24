#Approach 1 - Use the first index, and compare counter outputs for every other index, output the anagrams to a list, remove them from the original list, and append the new list to a final list. Keep looping until finished
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalList = []
        while(len(strs)>0):
            anagramList = []
            removeIndices = []
            anagramList.append(strs[0])
            for i in range(1, len(strs)):
                if Counter(strs[0])==Counter(strs[i]):
                    anagramList.append(strs[i])
                    removeIndices.append(i)
            for index in sorted(removeIndices, reverse=True):
                strs.pop(index)
            strs.pop(0)
            finalList.append(anagramList)
        return finalList

#Approach 2 (optimized) - Create a dict where each key represents a sorted string, and anagrams of that are appended on
from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalList = defaultdict(list)
        for str in strs:
            key = tuple(sorted(str))
            finalList[key].append(str)
        finalList = list(finalList.values())
        return finalList