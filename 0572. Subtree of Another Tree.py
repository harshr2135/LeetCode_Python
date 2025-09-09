# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):   # fixed typo (subRtoot → subRoot)
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))  # fixed typo (subTree → subRoot)

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:   # both None → trees match
            return True
        if not root or not subRoot:    # one None but not both → mismatch
            return False

        if root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and 
                    self.sameTree(root.right, subRoot.right))

        return False

