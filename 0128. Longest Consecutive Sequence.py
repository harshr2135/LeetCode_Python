class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 in num_set:
                continue
            length = 0
            while num in num_set:
                num += 1
                length += 1
            count = max(count,length)

        return count