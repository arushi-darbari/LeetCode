class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len2=len(set(nums))
        return len(nums)!=len2
