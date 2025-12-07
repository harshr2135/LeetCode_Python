# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        ans = []

        def dfs(root):
            if root is None:
                return 

            path.append(str(root.val))
            if not root.left and not root.right:
                ans.append("->". join(path))

            else:
                dfs(root.left)
                dfs(root.right)
            path.pop()

        dfs(root)

        return ans
        