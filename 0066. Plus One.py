class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for d in digits:
            s += str(d)

        num = int(s)+1
        res = []
        for n in str(num):
            res.append(int(n))

        return res