class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1

        while(high>low):
            mid=(high+low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high=mid
            else:
                low=mid+1
        
        if high+1==len(nums) and nums[high]<target:
            return high+1
        
        else:
            return high
        
