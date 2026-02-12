class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        
        res = []

        for digit in num:
            while res and res[-1] > digit and k>0:
                res.pop()
                k -= 1

            res.append(digit)

        while k>0:
            res.pop()
            k -= 1

        ans = "".join(res).lstrip('0')
        return ans if ans else "0"