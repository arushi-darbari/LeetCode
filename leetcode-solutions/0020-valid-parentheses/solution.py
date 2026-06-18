class Solution:
    def isValid(self, s: str) -> bool:
        close_map={
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack=[]

        for bracket in s:
            if bracket in close_map:
                if not stack or stack.pop()!=close_map[bracket]:
                    return False
            
            else:
                stack.append(bracket)

        return not stack
