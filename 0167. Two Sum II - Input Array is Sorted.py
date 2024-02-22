class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        begin, end = 0, len(numbers) - 1
        while begin < end:
            sum = numbers[begin] + numbers[end]
            if sum == target:
                return [begin + 1, end + 1]
            elif sum < target:
                begin += 1
            else:
                end -= 1