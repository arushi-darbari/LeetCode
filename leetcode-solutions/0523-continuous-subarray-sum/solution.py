from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # total=sum(nums)
        # temp_sum=0
        # sum_freq=defaultdict(int)
        # flag= False
        # sum_freq[0]=1
        # for i, value in enumerate(nums):
        #     temp_sum+=value
        #     if temp_sum-k in sum_freq or (temp_sum-k)%k==0:
        #         flag=True
            
        #     sum_freq[temp_sum]+=1

        # return flag

        temp_rem=0
        rem_freq=defaultdict(int)
        rem_freq[0]=-1
        temp_sum=0
        for i, value in enumerate(nums):
            temp_sum+=value
            temp_rem=temp_sum%k

            if temp_rem in rem_freq:
                if i-rem_freq[temp_rem]>1:
                    return True

            else:
                rem_freq[temp_rem]=i

        return False



        
