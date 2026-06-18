import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # line=s.lower().replace(" ","")
        line="".join(char for char in s if char not in string.punctuation).lower().replace(" ","")
        left=0
        right=len(line)-1
        while left<=right:
            if line[left]!=line[right]:
                return False
            else:
                left+=1
                right-=1
        
        return True

        
