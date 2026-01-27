class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0

        for idx in range(len(s)):
            if s[idx] == '(':
                depth += 1

            else:
                depth -= 1

                if s[idx-1] == '(':
                    score += 2**depth

        return score