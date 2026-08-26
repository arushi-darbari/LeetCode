class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length= float('-inf')
        seen=set()
        left=0
        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left+=1


            seen.add(s[right])
            length=max(length, right-left+1)

            # if s[right] not in seen:
            #     seen.add(s[right])
            #     length=max(length, right-left+1)

        return length if length!=float('-inf') else 0

