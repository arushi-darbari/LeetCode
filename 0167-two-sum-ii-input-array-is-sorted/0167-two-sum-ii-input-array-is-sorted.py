class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left= 0
        right= len(numbers)-1
        sum=0
        while(left<right):
            sum=numbers[left]+numbers[right]
            if sum<target:
                left+=1
            elif sum>target:
                right-=1
            elif sum==target:
                return [left+1,right+1]
        