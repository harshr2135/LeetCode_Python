class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c = 0,1,1
        if n == 0:
            return 0
        elif n == 1 or n ==2 :
            return 1
        elif n == 3 :
            return 2

        sum = a+b+c
        i = 3
        while i<=n:
            sum = a+b+c
            c,b,a = sum,c,b
            i += 1

        return sum