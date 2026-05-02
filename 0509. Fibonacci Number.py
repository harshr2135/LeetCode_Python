class Solution:
    def fib(self, n: int) -> int:
        Fn2 = 0
        Fn1 = 1

        fib = 0

        if n == 0:
            return Fn2
        elif n == 1:
            return Fn1
        else:
            for iter in range(2,n+1):
                Fn = Fn1 + Fn2
                Fn1, Fn2 = Fn, Fn1

        return Fn