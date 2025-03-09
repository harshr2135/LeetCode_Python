#Solution 1:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
    
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
    
        return False


#Solution 2:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)