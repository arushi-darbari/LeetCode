class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i

        if nums[0]==max(nums) or nums[-1]==max(nums) :
            return nums.index(max(nums))
        
