from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen=defaultdict(int)
        for i, value in enumerate(numbers):
            balance=target-value
            if balance in seen:
                return [seen[balance]+1,i+1]

            seen[value]=i

            
