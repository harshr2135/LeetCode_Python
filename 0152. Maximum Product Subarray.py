class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = minProd = result = nums[0]

        for iter in range(1, len(nums)):
            n = nums[iter]

            tempMax = max(n, n * maxProd, n * minProd)
            minProd = min(n, n * maxProd, n * minProd)
            maxProd = tempMax

            result = max(result, maxProd)

        return result
