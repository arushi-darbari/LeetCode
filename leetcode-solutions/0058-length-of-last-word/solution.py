class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st=s.strip()
        count=0
        for char in st[::-1]:
            if char==" ":
                break
            
            count+=1

        return count
