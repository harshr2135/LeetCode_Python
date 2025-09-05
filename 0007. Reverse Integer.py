class Solution:
    def reverse(self, x: int) -> int:
        
        neg = False
        if x<0:
            neg = True
            x = abs(x)

        rev = 0
        while x:
            rev = rev*10 + x%10
            x //= 10

        if rev > 2**31 -1 or rev < -2**31:
            return 0

        if neg:
            return -rev

        return rev
    
# class Solution:
#     def reverse(self, x: int) -> int:
#         ans = 0
#         sign = -1 if x < 0 else 1
#         x *= sign

#         while x:
#             ans = ans * 10 + x % 10
#             x //= 10

#         return 0 if ans < -2**31 or ans > 2**31 - 1 else sign * ans