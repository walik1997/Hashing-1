# time complexity O(n⋅klogk) where k is length of string 
#space Complexity - O(n)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        a=defaultdict(list)
        for i in strs:
            b=tuple(sorted(i))
            a[b].append(i)
        return a.values()