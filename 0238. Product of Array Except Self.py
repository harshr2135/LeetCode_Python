class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsSize = len(nums)
        res = [1] * numsSize

        for i in range(1, numsSize):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1
        for i in range(numsSize - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res