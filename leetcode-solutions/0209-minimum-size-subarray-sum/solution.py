class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length= float('inf')
        temp_sum=0
        left=0
        for right in range (len(nums)):
            temp_sum+=nums[right]
            while temp_sum>=target:
                length=min(length, right-left+1)
                temp_sum-=nums[left]
                left+=1

        return length if length!=float('inf') else 0
