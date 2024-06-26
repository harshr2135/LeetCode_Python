class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []
        for c in range(ord(s[0]), ord(s[-2])+1):
            for r in range(int(s[1]), int(s[-1])+1):
                res.append(chr(c)+str(r))

        return res