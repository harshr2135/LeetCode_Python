class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = 0
        count = 0

        prevSum = {0:1}

        for num in nums:
            prefixSum += num

            if prefixSum - goal in prevSum:
                count += prevSum[prefixSum - goal]

            prevSum[prefixSum] = prevSum.get(prefixSum, 0) + 1

        return count