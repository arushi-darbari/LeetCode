from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram=defaultdict(list)
        result=[]
        for index, value in enumerate(strs):
            key=tuple(sorted(value))
            anagram[key].append(value)
        
        result=list(anagram.values())

        return result
            
        
