class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for char in s:
            if char not in ["*", "#", "%"]:
                res.append(char)
            elif char == '*':
                if res:
                    res.pop()
            elif char == "#":
                res.extend(res)
            else:
                res.reverse()

        return ''.join(res)