class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        beg, end = 0, len(nums)-1
        mid = 0
        while beg<end:
            mid = (beg+end)//2
            if nums[mid] == target:
                return mid
            elif target<nums[mid]:
                end = mid-1
            else:
                beg = mid+1
            
        if nums[beg]<target:
            return beg+1
        return beg