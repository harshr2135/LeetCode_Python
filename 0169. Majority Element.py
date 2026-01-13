class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majElement = None

        for num in nums:
            if count == 0:
                majElement = num
            count += (1 if majElement == num else -1)

        if nums.count(majElement) > len(nums)//2:
            return majElement

        return -1