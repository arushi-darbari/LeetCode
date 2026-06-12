class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        arr={}
        for index,value in enumerate(nums):
            e1=target-value
            if e1 in arr:
                return [arr[e1],index]
            arr[value]=index
        
        

        
        
