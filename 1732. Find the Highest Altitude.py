class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum = list(accumulate(gain, initial = 0))

        high = prefixSum[0]

        for alt in prefixSum:
            if alt>high:
                high = alt

        return high
        