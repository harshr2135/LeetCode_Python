class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        stack = []

        for brac in s:
            if brac is '(':
                stack.append(brac)

            if brac is ')':
                if not stack:
                    count += 1
                    continue
                
                else: 
                    stack.pop()

        if stack:
            count += len(stack)
            
        return count