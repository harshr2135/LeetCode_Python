class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        idx = 0
        while idx<len(s):
            if res and s[idx] == '*':
                res.pop()
            else:
                res.append(s[idx])
            idx += 1
        
        return "".join(res)