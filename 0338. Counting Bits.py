class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for iter in range(1, n+1):
            ans.append(ans[iter>>1] + (iter&1))

        return ans