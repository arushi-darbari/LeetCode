class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_prefix_sum=0
        min_prefix=0
        max_sum=float('-inf')
        for num in nums:
            current_prefix_sum+=num
            max_sum=max(max_sum,current_prefix_sum-min_prefix)
            min_prefix=min(min_prefix, current_prefix_sum)

        return max_sum

