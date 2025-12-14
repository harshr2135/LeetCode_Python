class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        checkBit = 0

        for n in nums:
            mask = 1 << n
            if checkBit & mask:
                return n
            checkBit |= mask