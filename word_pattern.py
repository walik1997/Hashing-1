# time complexity -O(m) 
#space Complexity - O(m+n)
from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a=defaultdict(list)
        reva=defaultdict(list)
        sep= s.split(" ")
        b=tuple(sep)
        if len(b)!=len(pattern):
            return False
        else:
            for i in range(len(pattern)):
                if pattern[i] in a.keys() and a[pattern[i]] != b[i]:
                    return False 
                if  b[i] in reva.keys()  and reva[b[i]] != pattern[i] :
                    return False
                else:
                    a[pattern[i]]=(b[i])
                    reva[b[i]]=(pattern[i])               
            return True