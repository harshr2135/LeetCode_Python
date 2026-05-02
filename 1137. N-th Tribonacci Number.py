class Solution:
    def tribonacci(self, n: int) -> int:
        Tn3, Tn2, Tn1 = 0, 1, 1

        Tn = 0

        if n == 0:
            return Tn3
        elif n == 1:
            return Tn2
        elif n == 2:
            return Tn1
        else:
            for iter in range(3, n+1):
                Tn = Tn1 + Tn2 + Tn3
                Tn1, Tn2, Tn3 = Tn, Tn1, Tn2

        return Tn