class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        large, secLarge = 0, 0
        for n in nums:
            if large <= n:
                secLarge = large
                large = n
            elif secLarge < n:
                secLarge = n

        return (large-1)*(secLarge-1)
            