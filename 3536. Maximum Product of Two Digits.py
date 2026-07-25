class Solution:
    def maxProduct(self, n: int) -> int:
        first = second = 0

        nums = [int(num) for num in str(n)]

        for digit in nums:
            if digit >= first:
                second = first
                first = digit

            elif digit > second:
                second = digit

        return first * second