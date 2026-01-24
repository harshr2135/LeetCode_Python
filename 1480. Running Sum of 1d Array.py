class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefSum = [0] * len(nums)

        prefSum[0] = nums[0]

        for idx in range(1, len(nums)):
            prefSum[idx] = prefSum[idx-1] + nums[idx]

        return prefSum