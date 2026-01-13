class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        left = 0
        right = len(nums)-1
        currPos = len(nums)-1

        while left<=right:
            if abs(nums[left]) > abs(nums[right]):
                res[currPos] = nums[left]**2
                left += 1
            
            else:
                res[currPos] = nums[right]**2
                right -= 1
            
            currPos -= 1

        return res