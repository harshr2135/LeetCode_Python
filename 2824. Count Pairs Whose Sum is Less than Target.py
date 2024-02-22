class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # count = 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i]+nums[j])<target:
        #             count += 1

        # return count


        nums.sort()
        beg, end = 0, len(nums)-1
        count = 0
        while beg<=end:
            if(nums[beg]+nums[end]) < target:
                count += end-beg
                beg += 1
            else:
                end -= 1

        return count