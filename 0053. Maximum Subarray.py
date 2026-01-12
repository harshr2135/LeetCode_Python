class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = maxSum = nums[0]

        for iter in range(1, len(nums)):
            currSum = max(currSum+nums[iter], nums[iter])
            maxSum = max(maxSum, currSum)

        return maxSum