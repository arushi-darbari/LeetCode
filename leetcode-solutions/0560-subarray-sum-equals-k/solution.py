from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_freq=defaultdict(int)
        sum_freq[0]=1
        count=0
        temp_sum=0
        for i, value in enumerate (nums):
            temp_sum+=value
            if temp_sum-k in sum_freq:
                count+=sum_freq[temp_sum-k]
            
            sum_freq[temp_sum]+=1
        
        return count

