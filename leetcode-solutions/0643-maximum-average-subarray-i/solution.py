class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp_sum=0
        max_sum=float('-inf')
        left=0
        for right in range(len(nums)):
            temp_sum+=nums[right]
            if right-left+1>k:
                temp_sum-=nums[left]
                left+=1

            if right-left+1==k and temp_sum>max_sum:
                max_sum=temp_sum
        
        return max_sum/k


