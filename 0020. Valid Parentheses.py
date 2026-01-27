class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            else:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()

        return not stack


# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []

#         for brac in s:
#             if brac in ['(', '{', '[']:
#                 stack.append(brac)

#             else:
#                 if not stack:
#                     return False
#                 if brac == ')' and stack[-1] == '(':
#                     stack.pop()
#                 elif brac == '}' and stack[-1] == '{':
#                     stack.pop()
#                 elif brac == ']' and stack[-1] == '[':
#                     stack.pop()
#                 else:
#                     return False

#         return not stack