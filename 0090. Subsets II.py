class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(idx, curr):
            res.append(curr.copy())

            # backtrack(idx+1, curr)

            for iter in range(idx, len(nums)):
                if  iter>idx and nums[iter] == nums[iter-1]:
                    continue

                curr.append(nums[iter])
                backtrack(iter+1, curr)
                curr.pop()

        backtrack(0, [])
        return res