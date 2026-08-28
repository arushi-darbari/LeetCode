class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, value in enumerate (nums):
            if i!=value:
                return i

            if value==len(nums)-1:
                return value+1
