class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        arr={}
        for index, value in enumerate(nums):
            temp=target-value
            if temp in arr:
                return (index,arr[temp])
            else:
                arr[value]=index
