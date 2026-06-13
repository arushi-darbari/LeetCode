from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         anagram=defaultdict(list)
         for value in strs:
            sorted_s=tuple(sorted(value))
            anagram[sorted_s].append(value)
        
         return list(anagram.values())
