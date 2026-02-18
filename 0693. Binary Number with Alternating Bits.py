class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        nXOR = n ^ (n>>1)
        return (nXOR & nXOR+1) == 0