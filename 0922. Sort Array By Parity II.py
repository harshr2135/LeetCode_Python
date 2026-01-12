class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        even = 0
        odd = 1

        for num in nums:
            if num & 1 == 0:
                res[even] = num
                even += 2

            else:
                res[odd] = num
                odd += 2
        
        return res