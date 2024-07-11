class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        ans = []

        for ch in s:
            if ch == '(':
                stack.append(len(ans))
            elif ch == ')':
                j = stack.pop()
                ans[j:] = ans[j:][::-1]
            else:
                ans.append(ch)

        return ''.join(ans)