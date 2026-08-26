from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(1,len(nums)):
        #         if nums[i]+nums[j]==target and i!=j:
        #             return [i,j]
        
        arr=defaultdict(int)

        for index,value in enumerate(nums):
            ele=target-value
            if ele in arr:
                return [index,arr[ele]]
            
            else:
                arr[value]=(index)
