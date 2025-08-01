class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        split_path = path.split('/')

        for directory in split_path:
            if directory in('', '.'):
                continue
            if directory == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(directory)

        simplified_path = '/'.join(stack)
        return '/'+simplified_path
