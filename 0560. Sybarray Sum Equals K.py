class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        count = 0

        prevSum = {0:1}

        for num in nums:
            prefixSum += num

            if prefixSum - k in prevSum:
                count += prevSum[prefixSum - k]

            prevSum[prefixSum] = prevSum.get(prefixSum, 0) + 1

        return count