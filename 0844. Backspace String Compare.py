class Solution:
    def stackOp(self, string):
        res = []

        for ch in string:
            if ch == '#':
                if res:
                    res.pop()
            else:
                res.append(ch)
        
        return "".join(res)

    def backspaceCompare(self, s: str, t: str) -> bool:
        clean_s = self.stackOp(s)
        clean_t = self.stackOp(t)

        return clean_s == clean_t