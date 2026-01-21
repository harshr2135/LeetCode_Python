class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        count = 0

        prevDiv = {0:1}

        for num in nums:
            prefixSum += num
            remainder = prefixSum % k
            
            if prefixSum % k in prevDiv:
                count += prevDiv[remainder]

            prevDiv[remainder] = prevDiv.get(remainder, 0) + 1

        return count