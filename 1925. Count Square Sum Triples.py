class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        squares = {i**2 for i in range(1, n+1)}

        for a in squares:
            for b in squares:
                if (a+b) in squares:
                    res += 1

        return res